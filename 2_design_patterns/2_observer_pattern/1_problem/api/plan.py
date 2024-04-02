from .lib.db import find_user
from .lib.slack import post_slack_message
from .lib.email import send_email
from .lib.log import log


def upgrade_plan(email: str):
    user = find_user(email)

    user.plan = "paid"

    post_slack_message("sales", f"{user.name} has upgraded their plan.")

    send_email(user.name, user.email, "Thank you", f"Thanks for upgrading, {user.name}! You are gonna love it. \nRegards, The DevNotes Team")

    log(f"User with email address {user.email} has upgraded their plan")

