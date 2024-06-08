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
    new_index = len(register_dict)
    register_dict[new_index] = {"email": email, "password": password}
    save_json(json_name="users.json", data=register_dict)
    return True
