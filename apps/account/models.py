from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from apps.account.managers import CustomUserManager, ADMIN, USER


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        (ADMIN, 'Admin'),
        (USER, 'User')
    )

    username = None
    first_name = models.CharField(_('first name'), max_length=100, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.CharField('Тип пользователя', max_length=20, choices=USER_TYPE)

    is_superuser = models.BooleanField(_('superuser status'), default=False,
        help_text='Указывает, следует ли рассматривать этого пользователя как суперпользователя.')
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=False,
        help_text=_("Designates whether this user should be treated as active. "
                    "Unselect this instead of deleting accounts."), )

    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновлении', auto_now=True)

    activation_code = models.CharField(max_length=8, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Возвращает first_name плюс last_name с пробелом между ними.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def create_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(length=8,
                                 allowed_chars='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPSDFGHJKLZXCVBNM1234567890')
        self.activation_code = code

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
