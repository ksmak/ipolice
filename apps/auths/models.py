from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError("Логин не должен быть пустым")

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='логин',
        max_length=150,
        unique=True
    )
    name = models.CharField(
        verbose_name='фамилия',
        max_length=255,
        blank=True,
        null=True
    )
    surname = models.CharField(
        verbose_name='имя',
        max_length=255,
        blank=True,
        null=True
    )
    patronymic = models.CharField(
        verbose_name='отчество',
        max_length=255,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        verbose_name='активность',
        default=True
    )
    is_superuser = models.BooleanField(
        verbose_name='является администратором',
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name='является штатным сотрудником',
        default=False
    )
    date_of_creation = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    date_of_change = models.DateTimeField(
        verbose_name='дата изменения',
        auto_now=True
    )
    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
