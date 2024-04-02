from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan
from api.slack_listener import setup_slack_event_handler
from api.email_listener import setup_email_event_handlers
from api.log_listener import setup_log_event_handlers

setup_log_event_handlers()
setup_email_event_handlers()
setup_slack_event_handler()

register_new_user("Tarun", "tarun@gmail.com", "abcdef")

password_forgotten("tarun@gmail.com")

upgrade_plan("tarun@gmail.com")
