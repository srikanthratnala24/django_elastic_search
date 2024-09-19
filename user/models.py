from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError("User should have a username")
        
        if email is None:
            raise TypeError("User should have a Email")
        
        user = self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self,username,email,password=None):
        if password is None:
            raise TypeError("password should not be none")
        
        if email is None:
            raise TypeError("User should have a Email")
        user = self.create_user(username,email,password)
        user.is_superuser = True
        user.is_status = True
        user.save()

        return user
    

class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=200,unique=True,db_index=True)
    email = models.EmailField(max_length=255, unique=True,db_index=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usernmae',]

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh':str(refresh),
            'access':str(refresh.access_token)

        }
        

    

