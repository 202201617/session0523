from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_no_special_characters

class User(AbstractUser):
	nickname = models.CharField(
		max_length=15,
		unique=True,
		null = True,
		validators = [validate_no_special_characters],
		error_messages={'unique': '이미 사용중인 닉네임입니다.'},
	)
	
	def __str__(self):
		return self.email