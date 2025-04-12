from django.contrib import admin

# Register your models here.

from .models import Welcome,Banners
admin.site.register(Welcome)
admin.site.register(Banners)