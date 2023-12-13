import jwt
from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserProfileManager(BaseUserManager):
    """
    Defines user creation fields and manages to save user
    """

    def create_user(self, username, phone, telegram_pk, password=None):
        """
        Create User
        """
        if not username:
            raise ValueError('The Username must be set')
        if not phone:
            raise ValueError('The Phone number must be set')
        if not telegram_pk:
            raise ValueError('The Telegram ID must be set')

        user = self.model(
            username=username,
            phone=phone,
            telegram_pk=telegram_pk,
        )
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, phone, telegram_pk, password=None):
        """
        Create Staff User
        """
        user = self.create_user(
            username,
            phone,
            telegram_pk,
            password=password,
        )
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone, telegram_pk, password=None):
        """
        Create SUPER MAN User
        """
        user = self.create_user(
            username,
            phone,
            telegram_pk,
            password=password,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Creates a customized database table for user using customized user manager
    """
    username = models.CharField(
        verbose_name='Имя',
        unique=True,
        max_length=150,
    )
    phone = models.CharField(
        verbose_name='Номер',
        max_length=15,
    )
    telegram_pk = models.CharField(
        verbose_name='Телеграмм ID',
        max_length=20, 
        unique=True,
    )
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_admin = models.BooleanField(
        default=False
    )
    
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['phone', 'telegram_pk']

    objects = UserProfileManager()

    def str(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def token(self):
        return self.generate_jwt_token()

    def generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=45)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.strftime('%S')
        },
            settings.SECRET_KEY, algorithm='HS256').encode().decode('utf-8')

        return token