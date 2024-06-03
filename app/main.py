from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def submit(request: Request, email: str = Form(...), password: str = Form(...)):
    # Hier können Sie die Logik zur Verarbeitung der E-Mail und des Passworts hinzufügen
    # Zum Beispiel, die Daten speichern oder eine Bestätigungs-E-Mail senden

    # Redirect to the confirmation page with the email as a query parameter
    return RedirectResponse(url=f"/confirm_email?email={email}", status_code=303)

@app.get("/confirm_email", response_class=HTMLResponse)
async def confirm_email(request: Request, email: str):
    return templates.TemplateResponse("confirmation.html", {"request": request, "email": email})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})
