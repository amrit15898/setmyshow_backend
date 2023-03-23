from django.contrib import admin
from django.urls import path , include

from .views import *
urlpatterns = [
   
    path("get-event/", EventApi.as_view(), name="event_api")
]