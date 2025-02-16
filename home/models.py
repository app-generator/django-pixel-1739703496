# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    chat like  king = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Let Us Chat(models.Model):

    #__Let Us Chat_FIELDS__
    chat = models.TextField(max_length=255, null=True, blank=True)

    #__Let Us Chat_FIELDS__END

    class Meta:
        verbose_name        = _("Let Us Chat")
        verbose_name_plural = _("Let Us Chat")



#__MODELS__END
