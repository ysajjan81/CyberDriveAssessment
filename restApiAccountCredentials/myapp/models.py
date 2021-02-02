from django.db import models

class Users(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)