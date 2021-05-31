from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.icecream_detail),
    path('icecream-new/', views.icecream_new),
]
