from .lib.db import create_user, find_user
from .lib.stringtools import get_random_string
from .event import post_event


def register_new_user(name: str, email: str, password: str):
    user = create_user(name, email, password)

    post_event("user_registered", user)


def password_forgotten(email: str):
    user = find_user(email)

    user.reset_code = get_random_string(16)

    post_event("user_password_forgotten", user)
