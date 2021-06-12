from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.icecream_detail_pk),
    path('icecream-new/', views.icecream_new),
    path('icecream-detail/', views.icecream_detail, name = 'icecream_detail'),
]
