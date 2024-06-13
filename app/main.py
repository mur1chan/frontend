from typing import Optional

from fastapi import Depends, FastAPI, Form, Header, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from asgi_htmx import HtmxMiddleware
from asgi_htmx import HtmxRequest as Request
from app.backend_json import (
    login_user,
    register_user,
    return_article,
    return_titles,
    load_json,
)
from fastapi_login import LoginManager

app = FastAPI()
templates = Jinja2Templates(directory="templates")
components = Jinja2Templates(directory="templates/components")
app.add_middleware(HtmxMiddleware)

SECRET = "super-secret-key"

manager = LoginManager(
    SECRET, "/submit-login", use_cookie=True, cookie_name="access_token"
)


DB = load_json("users.json")

DB = load_json("users.json")


@manager.user_loader()
def load_user(email: str):
    # Return user dictionary if user with the email exists
    for user in DB.values():
        if user["email"] == email:
            return user
    return None


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit-register", response_class=HTMLResponse)
async def submit(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
):
    print(f"Received email: {email}, password: {password}")
    register_new_user = register_user(email=email, password=password)
    if register_new_user:
        print("User registered successfully.")
        return HTMLResponse(
            content="Registration successful. Check your email.", status_code=200
        )
    else:
        print("User registration failed.")
        return HTMLResponse(
            content="There is already a user with this email.", status_code=400
        )


@app.post("/submit-login")
async def submit_login(
    request: Request,
    response: Response,
    email: str = Form(...),
    password: str = Form(...),
):
    print(f"Received email: {email}, password: {password}")
    user = load_user(email)
    if user and user["password"] == password:
        print("Login successful.")
        token = manager.create_access_token(data={"sub": email})
        manager.set_cookie(response, token)
        return {"response": response}
    else:
        print("Login failed.")
        return HTMLResponse(content="Invalid email or password.", status_code=200)


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request, user=Depends(manager)):
    articles_dict = return_article()
    context = {
        "request": request,
        "title": articles_dict["title"],
        "authors": articles_dict["authors"],
        "abstract": articles_dict["abstract"],
    }
    return templates.TemplateResponse("home.html", context)


@app.get("/confirm_email", response_class=HTMLResponse)
async def confirm_email(request: Request, email: str):
    return templates.TemplateResponse(
        "confirmation.html", {"request": request, "email": email}
    )


@app.get("/research-experience", response_class=HTMLResponse)
async def research_experience(request: Request):
    titles_dict = return_titles()
    context = {
        "request": request,
        "research_experience": titles_dict["title_1"],
    }
    return templates.TemplateResponse("research_experience.html", context)


@app.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    articles_dict = return_article()
    titles_dict = return_titles()
    context = {
        "request": request,
        "research_experience": titles_dict["title_1"],
        "education": titles_dict["title_2"],
        "contact_details": titles_dict["title_3"],
        "title": articles_dict["title"],
        "authors": articles_dict["authors"],
        "abstract": articles_dict["abstract"],
    }
    return templates.TemplateResponse("profile.html", context)


@app.get("/test-publication", response_class=HTMLResponse)
async def articles(request: Request):
    articles_dict = return_article()
    context = {
        "request": request,
        "title": articles_dict["title"],
        "authors": articles_dict["authors"],
        "abstract": articles_dict["abstract"],
    }
    return templates.TemplateResponse("test_publication.html", context)


"""
THIS IS AN EXAMPLE HOW TO USE HTMX WITH FASTAPI
"""


@app.get("/htmx", response_class=HTMLResponse)
async def htmx(request: Request):
    return templates.TemplateResponse("htmx_test.html", {"request": request})


@app.get("/htmx-get-test", response_class=HTMLResponse)
async def htmx_get_fn(request: Request):
    scope = request.scope["htmx"]
    print(scope.target)
    print(scope.current_url)
    context = {
        "request": request,
        "htmx_name": "this is inhereted from htmx",
        "htmx_value": "this value is inhereted from htmx",
    }
    return components.TemplateResponse("result.html", context)


@app.get("/htmx-get-user-input", response_class=HTMLResponse)
async def htmx_get_user_input(request: Request):
    scope = request.scope["htmx"]
    # print(scope.target)
    # print(scope.current_url)
    # print(request.body)
    return templates.TemplateResponse("user_input.html", {"request": request})


# @app.post("/htmx-post-user-input", response_class=HTMLResponse)
# async def htmx_post_user_input(request: Request, user_input: str = Form(...)):
#     scope = request.scope["htmx"]
#     print(scope.target)
#     print(scope.current_url)
#     print(scope.)
