from django.contrib import admin

from .models import  Person, MapSession, UserVideoLink, Label


admin.site.register(Person)
admin.site.register(MapSession)
admin.site.register(UserVideoLink)
admin.site.register(Label)