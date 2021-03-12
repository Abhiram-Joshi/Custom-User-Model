from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **info):

        if not email:
            raise ValueError(ugettext_lazy('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **info)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **info):

        info.setdefault('is_staff', True)
        info.setdefault('is_superuser', True)
        info.setdefault('is_active', True)

        if info.get('is_staff') is not True:
            raise ValueError(ugettext_lazy('Superuser must have is_staff=True.'))
        if info.get('is_superuser') is not True:
            raise ValueError(ugettext_lazy('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **info)