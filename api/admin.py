# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import user
# Register your models here.

class userAdmin(UserAdmin):
	ordering = ('firstname',)

	list_display=('username','firstname','lastname','email')
	add_fieldsets = (
			('Personal Information',{
				'fields':('profilePic','username','is_superuser','email','firstname','lastname')
				}),
			('Contact Information',{
				'fields':('country')
			}),
			)
	fieldsets = (
		('Personal Information',{
				'fields':('username','is_superuser','email','firstname','lastname',)
				}),
			('Contact Information',{
				'fields':('country',)
			}),
		)
	
admin.site.register(user, userAdmin)
