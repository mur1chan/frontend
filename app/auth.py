from fastapi import FastAPI, Response

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
app = FastAPI()
SECRET = "super-secret-key"

manager = LoginManager(SECRET, "/login", use_cookie=True, cookie_name='access_token')

DB = {"users": {"johndoe@mail.com": {"name": "John Doe", "password": "hunter2"}}}


@manager.user_loader()
def query_user(user_id: str):
    """
    Get a user from the db
    :param user_id: E-Mail of the user
    :return: None or the user object
    """
    return DB["users"].get(user_id)

@app.post("/login")
def login(
        response: Response,
        data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = query_user(email)
    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif password != user["password"]:
        raise InvalidCredentialsException

    token = manager.create_access_token(data={"sub": email})
    manager.set_cookie(response, token)
    return {"access_token": token}

@app.get("/protected")
def protected_route(user=Depends(manager)):
    return {"user": user}
