# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# # SuperUserInformation
# # User: Jose
# # Email: training@pieriandata.com
# # Password: testpassword
#
#
# class Posts(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     created_at = models.DateTimeField(default=datetime.now, blank=True)
#     def __str__(self):
#         return self.title
#     class Meta:
#         verbose_name_plural = "Posts"
#
#
# class UserProfileInfo(models.Model):
#
#     # Create relationship (don't inherit from User!)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     # Add any additional attributes you want
#     portfolio_site = models.URLField(blank=True)
#     # pip install pillow to use this!
#     # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
#     profile_pic = models.ImageField(upload_to='basic_app/profile_pics',blank=True)
#
#     def __str__(self):
#         # Built-in attribute of django.contrib.auth.models.User !
#         return self.user.username
