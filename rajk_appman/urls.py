from django.urls import path, include
from . import views

app_name = "rajk-appman"
urlpatterns = [
    path("", views.home, name="home"),
    path("user_page", views.user_page, name="user_page"),
]
