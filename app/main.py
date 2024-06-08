from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Form, Header, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.backend_json import register_user

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
    hx_request: Optional["str"] = Header(None),
):
    register_new_user = register_user(email=email, password=password)
    if register_new_user:
        if hx_request:
            return RedirectResponse(
                url=f"/confirm_email?email={email}", status_code=303
            )
    else:
        return templates.TemplateResponse(
            "/components/error_register.html", {"request": request}
        )


@app.get("/confirm_email", response_class=HTMLResponse)
async def confirm_email(request: Request, email: str):
    return templates.TemplateResponse(
        "confirmation.html", {"request": request, "email": email}
    )


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
