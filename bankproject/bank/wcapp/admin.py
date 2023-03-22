from django.contrib import admin

from wcapp.models import  Person

# Register your models here.
mymodels=[Person]

admin.site.register(mymodels)
