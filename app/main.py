from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Form, Header, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.backend_json import login_user, register_user

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit", response_class=HTMLResponse)
async def submit(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    hx_request: Optional[str] = Header(None),
):
    print(f"Received email: {email}, password: {password}")
    register_new_user = register_user(email=email, password=password)
    if register_new_user:
        print("User registered successfully.")
        if hx_request:
            return RedirectResponse(
                url=f"/confirm_email?email={email}", status_code=303
            )
        else:
            return HTMLResponse(
                content="Registration successful. Check your email.", status_code=200
            )
    else:
        print("User registration failed.")
        return HTMLResponse(
            content="There is already a user with this email.", status_code=400
        )


@app.post("/submit_login", response_class=HTMLResponse)
async def submit_login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    hx_request: Optional[str] = Header(None),
):
    print(f"Received email: {email}, password: {password}")
    login_successful = login_user(email=email, password=password)
    print(f"login is {login_successful}")
    if login_successful == True:
        print("Login successful.")
        return HTMLResponse(content="Login successful.", status_code=200)
    elif login_successful == False:
        print("Login failed.")
        return HTMLResponse(content="Invalid email or password.", status_code=400)


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/confirm_email", response_class=HTMLResponse)
async def confirm_email(request: Request, email: str):
    # Rendern Sie die Bestätigungsseite und geben Sie die E-Mail-Adresse an das Template weiter
    return templates.TemplateResponse(
        "confirmation.html", {"request": request, "email": email}
    )

@app.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})