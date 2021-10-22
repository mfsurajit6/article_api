from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    """ Custom Manager Class to create User and Superuser"""

    def create_user(self, email, name='',password=None):
        if not email:
            raise TypeError('User must have an email')
        
        user = self.model(name=name, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password=None):
        if password is None:
            raise TypeError('Superuser must have a password')
        user = self.create_user(email, name=name, password=password)
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Model"""

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['name', ]
    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser
    
    def clean(self):
        if self.email is not None:
            self.email = self.email.lower()
        return super(User, self).clean()
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return '<User: {}>'.format(self.name)

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
