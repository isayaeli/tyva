from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.

USER_STATUS = (
    ('Manager','Manager'),
    ('Not a Manager','Not a Manager')
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='profile_pics',null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    user_status =models.CharField(max_length=100,default='Not a Manager', choices=USER_STATUS)
    created = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(default=User, unique=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
         self.slug = slugify(self.user.username)
         super(Profile, self).save(*args, **kwargs)



def create_profile(sender, **kwargs):
    if kwargs['created']:
       profile = Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)