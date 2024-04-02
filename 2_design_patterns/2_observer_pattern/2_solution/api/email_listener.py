from .lib.email import send_email
from .event import subscribe


def handle_user_registered_event(user):
    send_email(user.name, user.email, "Welcome", f"Thanks for registering, {user.name}!\nRegards, The DevNotes Team")


def handle_user_password_forgotten_event(user):
    send_email(user.name, user.email, "Reset your password",
               f"To reset your password, use this secure code {user.reset_code}.\nRegards, The DevNotes Team")


def handle_user_upgrade_plan_event(user):
    send_email(user.name, user.email, "Thank you",
               f"Thanks for upgrading, {user.name}! You are gonna love it. \nRegards, The DevNotes Team")


def setup_email_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_user_password_forgotten_event)
    subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)
