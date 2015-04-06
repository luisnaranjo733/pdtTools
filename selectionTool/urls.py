from django.conf.urls import include, url
from django.contrib import admin

from selectionTool import views

urlpatterns = [
    url(r'^$', views.home),
]
