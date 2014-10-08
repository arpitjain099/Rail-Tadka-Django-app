from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Menu(models.Model):
    item = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    cost = models.IntegerField(default=0)
    itype = models.CharField(max_length=50) 
# Create your models here.
