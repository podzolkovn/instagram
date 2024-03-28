from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, verbose_name='phone number', blank=True, null=True)
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name='email address')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile', verbose_name='profile')
    avatar = models.ImageField(default='avatars/default.jpeg', upload_to='avatars', verbose_name='avatar', null=True,
                               blank=True)
    description = models.TextField(verbose_name='description', blank=True, null=True)
    gender = models.CharField(max_length=15, verbose_name='gender', blank=True, null=True)


class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following_set')
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers_set')

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower} follows {self.following}'

