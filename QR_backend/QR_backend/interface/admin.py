from django.contrib import admin
from .models import teacher

def reg(mod):
    return admin.site.register(mod)

reg(teacher)
