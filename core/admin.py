from django.contrib import admin

from .models import app_models


for model in app_models:
    admin.site.register(model)