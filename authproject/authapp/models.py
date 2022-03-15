from webbrowser import get
from django.db import models
from django.contrib.auth import get_user_model
from allauth.account.signals import user_logged_in 

User=get_user_model()

# Create your models here.
def user_logged_in_receiver(request, user, **kwargs):
    print(request)
    print(user)
    
user_logged_in.connect(user_logged_in_receiver, sender=User)