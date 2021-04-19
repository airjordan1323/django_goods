from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
from datetime import datetime


class MyAccoutManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Пользователь должен иметь электронный адресс!")
        if not username:
            raise ValueError("Пользватель должен иметь логин!")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_journalist = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    name = models.CharField("Ваше имя", max_length=30, unique=True)
    surname = models.CharField("Ваше фамилия", max_length=30, unique=True)
    username = models.CharField("Имя для входа", max_length=30, unique=True)
    email = models.EmailField("Электронный адрес", unique=True)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField("Аватар пользователя", upload_to="avatar/")
    date_joined = models.DateTimeField("Дата регистрации", auto_now_add=datetime.now())
    gender = models.CharField(max_length=10, choices=GENDER, default='male')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_journalist = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    objects = MyAccoutManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True
