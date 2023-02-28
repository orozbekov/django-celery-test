from django.contrib.auth.base_user import BaseUserManager


ADMIN: str = 'admin'
USER: str = 'user'


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.create_activation_code()
        user.save(self._db)

        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('user_type', USER)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('user_type', ADMIN)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )
        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )

        return self._create_user(email, password, **extra_fields)
