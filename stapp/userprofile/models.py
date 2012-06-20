from django.db import models
from django.contrib.auth.models impport User

# Create your models here.

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	

	

	
