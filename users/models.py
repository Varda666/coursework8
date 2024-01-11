
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.timezone import now


class MyUserManager(UserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
        user = User.objects.create(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    member = 'member'
    USER_ROLE_CHOISES = [
        ('member', 'member'),
        ('moderator', 'moderator'),
        ('owner', 'owner')
    ]

    username = None
    first_name = None
    last_name = None
    user_role = models.CharField(
        choices=USER_ROLE_CHOISES,
        default=member,
        verbose_name='роль'
    )
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(max_length=150, verbose_name='имя')
    last_login = models.DateField(
        default=now, verbose_name='дата последнего посещения'
    )
    is_staff = models.BooleanField(default=False, verbose_name="статус staff")
    is_active = models.BooleanField(
        default=True, verbose_name="статус активности"
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
