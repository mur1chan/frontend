import json
from typing import List, Tuple
import secrets
from typing_extensions import Dict


def load_json(json_name: str) -> Dict:
    with open(json_name, "r") as target:
        return json.load(target)


def save_json(json_name: str, data: Dict):
    with open(json_name, "w") as target:
        json.dump(data, target, indent=4)


def append_json(json_name: str, data: Dict):
    with open(json_name, "a") as target:
        json.dump(data, target, indent=4)


def register_user(name: str, email: str, password: str) -> bool:
    register_dict = load_json("users.json")

    # Check if the email already exists in the register_dict
    for user_index, user_data in register_dict.items():
        print(f'checking {user_data["email"]} with loaded {email}')
        if user_data["email"] == email:
            print(f'{user_data["email"]} already registered')
            return False

    # If the email does not exist, add the new user
    new_index = str(len(register_dict))
    register_dict[new_index] = {
        "name": name,
        "email": email,
        "password": password,
        "profile_picture": "",
        "topics": [],
        "skills": [],
    }
    save_json("users.json", register_dict)
    print(f"{email} registered successfully")
    return True


def load_session(token: str):
    """
    need token of user to return email
    """
    session_dict = load_json("session.json")
    session_info = session_dict.get(token)
    if session_info:
        return session_info
    else:
        return False


def save_session(token: str, email: str):
    """
    save the session of the user as identifier
    token and email are required
    """
    sessions = load_json("session.json")
    sessions[token] = email
    save_json("session.json", sessions)
    print(f"{email} with token: {token} successfully logged")
    return True


def load_profile(user_id: str):
    users_dict = load_json("users.json")
    print(users_dict[user_id])
    return users_dict[user_id]


def login_user(email: str, password: str) -> bool:
    users_dict = load_json("users.json")
    max_register_dict = len(users_dict)

    for user_index in range(0, max_register_dict):
        user_dict = users_dict[str(user_index)]
        print(user_dict["email"], user_dict["password"])
        if user_dict["email"] == email and user_dict["password"] == password:
            return True  # Wenn Benutzer gefunden wurde, ist die Anmeldung erfolgreich
    return False  # Ansonsten ist die Anmeldung fehlgeschlagen


def return_article():
    articles_dict = load_json("articles.json")
    secrange = secrets.SystemRandom().randint(1, len(articles_dict) - 1)
    return articles_dict[str(secrange)]


def return_titles():
    titles_dict = load_json("titles.json")
    return titles_dict


def save_user_articles(title: str, article_body: str):
    users_articles_dict = load_json("users_articles.json")
    new_index = str(len(users_articles_dict))

    users_articles_dict[new_index] = {"title": title, "article_body": article_body}
    save_json("users_articles.json", users_articles_dict)
