# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors["fname"] = "First name must be more than 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "Last Name must be more than 2 characters"
        if len(postData['email']) < 10:
            errors["email"] = "Email must be more than 10 characters"
        return errors;

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
