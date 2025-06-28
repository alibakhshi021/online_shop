from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile', verbose_name='تصویر آواتار', blank=True, null=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    about_name = models.TextField(blank=True, null=True, verbose_name='اطلاعات شخص')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')
    email = models.EmailField(max_length=100, unique=True)
    # password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        return self.email

#Model Api TEST
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)    
    last_name = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return self.user.email