from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	title=models.CharField(max_length=200)
	sub_title=models.CharField(max_length=200)