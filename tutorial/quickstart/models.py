from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserCustom(User):
    test_key = models.CharField(max_length=100, null=True, blank=True)
