from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)

    def get_username(self):
        return self.email
