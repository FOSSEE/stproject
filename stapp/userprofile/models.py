from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
	('Female', 'Female'),
	('Male' , 'Male'),	
	)

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	dob = models.DateField(auto_now=False)
	gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
	
	def __unicode__(self):
	    return u"%s the place" % self.user.username


	
	
	

	

	
