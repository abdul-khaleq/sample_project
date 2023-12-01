
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products/', views.products),
    path('contact/', views.contact),
    path('about/', views.about),
]