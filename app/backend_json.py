import json
import typing
from pprint import pprint

from typing_extensions import Dict


def load_json(json_name: str) -> Dict:
    with open(json_name, "r") as target:
        return json.load(target)


def save_json(json_name: str, data: Dict):
    with open(json_name, "w") as target:
        json.dump(data, target, indent=4)


def register_user(email: str, password: str) -> bool:
    register_dict = load_json("users.json")

    # Check if the email already exists in the register_dict
    for user_index, user_data in register_dict.items():
        print(f'checking {user_data["email"]} with loaded {email}')
        if user_data["email"] == email:
            print(f'{user_data["email"]} already registered')
            return False

    # If the email does not exist, add the new user
    new_index = str(len(register_dict))
    register_dict[new_index] = {"email": email, "password": password}
    save_json("users.json", register_dict)
    print(f"{email} registered successfully")
    return True


def login_user(email: str, password: str) -> bool:
    users_dict = load_json("users.json")
    max_register_dict = len(users_dict)

    for user_index in range(0, max_register_dict):
        user_dict = users_dict[str(user_index)]
        if user_dict["email"] == email and user_dict["password"] == password:
            return True  # Wenn Benutzer gefunden wurde, ist die Anmeldung erfolgreich
    return False  # Ansonsten ist die Anmeldung fehlgeschlagen


def return_article():
    articles_dict = load_json("articles.json")
    return articles_dict["0"]
