from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan


register_new_user("Tarun", "tarun@gmail.com", "abcdef")

password_forgotten("tarun@gmail.com")

upgrade_plan("tarun@gmail.com")
