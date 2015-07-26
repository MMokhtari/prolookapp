from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

IN_OUT = (('IN','In'),('OUT','Out'))
class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )
        
        account.is_admin = True

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.is_super_staff = True
        account.is_staff = True
        account.save()

        return account
        
class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    tagline = models.CharField(max_length=140, blank=True)

    is_admin = models.BooleanField(default=False)
    is_super_staff = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    access_granted = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name
    @property
    def phones(self):
        return self.phone_set.all()
    def addresses(self):
        return self.address_set.all()
    def company(self):
        return self.company_set.all()

class Phone(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Iccorect phone number")
    phone_number = models.CharField(max_length=16,validators=[phone_regex], blank=True) # validators should be a list
    account = models.ForeignKey(Account)
    def __str__(self):
        return self.phone_number
class Address(models.Model):
    line = models.CharField(max_length = 200, blank = True)
    account = models.ForeignKey(Account)
    def __str__(self):
        return self.line
class Company(models.Model):
    name = models.CharField(max_length=50,blank=False)
    domain = models.CharField(max_length=70,blank=True)
    account = models.ForeignKey(Account)
    def __str__(self):
        return self.name
class CompanyMileStone(models.Model):
    """docstring for CompanyMileStone"""
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(default='')
    def __str__(self):
        return self.title

class Team(models.Model):
    """docstring for Team"""
    name = models.CharField(unique=True,max_length=50,blank=False)
    description = models.TextField()
    account = models.ForeignKey(Account)
    def __str__(self):
        return self.name

class AccountTrack(models.Model):
    """docstring for AccountTrack"""
    account = models.ForeignKey(Account)
    log = models.DateTimeField()
    in_out = models.CharField(choices=IN_OUT,max_length=20)
    def __str__(self):
        return self.account