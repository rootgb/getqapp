from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, help_text = "")
	
	def __unicode__(self):
		return self.user.username

class Event(models.Model):
					name= models.CharField(max_length=50)
					code= models.CharField(max_length=50,unique=True)
					start= models.DateTimeField(default=datetime.now, blank=True)
					end = models.DateTimeField(default=datetime.now, blank=True)


class Question(models.Model):
    event = models.ForeignKey(Event)
    q_1 = models.CharField(max_length = 100)
    q_2 = models.CharField(max_length = 100)
    q_3 = models.CharField(max_length = 100)
    created = models.DateTimeField(default=datetime.now, blank=True)

class Response(models.Model):
    event = models.ForeignKey(Event)
    a_1 = models.IntegerField()
    a_2 = models.IntegerField()
    a_3 = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
