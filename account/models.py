from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone_number,room_number, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not phone_number:
            raise ValueError("Users must have a phone number")
        if not room_number:
            raise ValueError("Users must have a room number")

        user = self.model(
               email = self.normalize_email(email),
               username=username,
               first_name=first_name,
               last_name=last_name,
               phone_number=phone_number, 
               room_number=room_number, 
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, username, phone_number, room_number,password):
        user = self.create_user(
               email = self.normalize_email(email),
               password=password,
               first_name=first_name,
               last_name=last_name,
               phone_number=phone_number,
               username=username, 
               room_number=room_number,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email                       = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username                    = models.CharField(max_length=30, unique=True)
    first_name                  = models.CharField(max_length=30, verbose_name="first name")
    last_name                   = models.CharField(max_length=30, verbose_name="last name")
    phone_number                = models.CharField(max_length=11, verbose_name="phone number", unique=True)
    room_number                 = models.CharField(max_length=11, verbose_name="room number")
    date_joined                 = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login                  = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                    = models.BooleanField(default=False)
    is_active                   = models.BooleanField(default=True)
    is_staff                    = models.BooleanField(default=False)
    is_superuser                = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username', 'first_name', 'last_name', 'phone_number', 'room_number']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True





