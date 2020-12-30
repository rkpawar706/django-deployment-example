from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    #add the additional fields
    portfolio_site = models.URLField(blank=True)
    profile_image = models.ImageField(blank=True,upload_to='profilepics')

    def __str__(self):
        return self.user.username


