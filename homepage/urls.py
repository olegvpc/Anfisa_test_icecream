from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path("friend/", views.new_friend, name = "new_friend"),
]
