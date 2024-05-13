# Register your models here.

from django.contrib import admin

from .models import Coords, Pereval, Users

admin.site.register(Coords)
admin.site.register(Pereval)
admin.site.register(Users)
