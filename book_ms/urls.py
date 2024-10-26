from . import views

from django.urls import path

urlpatterns = [
    path('', views.home, name="homepage"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    
      
]
