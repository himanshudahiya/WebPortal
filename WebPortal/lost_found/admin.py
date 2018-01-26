from django.contrib import admin
from .models import users,lostEntry,foundEntry

admin.site.register(users)
admin.site.register(lostEntry)
admin.site.register(foundEntry)