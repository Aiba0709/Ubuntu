from django.urls import path

from users.views import register

urlpatterns = [
    path("user/register/", register, name="register")
]