from django.contrib import admin
from django.urls import path , include

from .views import *
urlpatterns = [
    path("login", artist_login),
    path("get-users/",SignupApi.as_view()),
    path("get-single/<id>", GetSingleUser.as_view()),
    path("person-api", PersonApi.as_view())
    
]