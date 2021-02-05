from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
# receiver
def login_success(sender, request, user,  **kwargs):
    print("_--------------------")
    print("logged in Signal ..... Run intro")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print(f'Kwargs: {kwargs}')

user_logged_in.connect(login_success, sender=User)

