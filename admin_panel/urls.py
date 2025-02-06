# api/urls.py
from django.urls import path
from .views import AdminLoginView

urlpatterns = [
   path('login/', AdminLoginView.as_view(), name='admin-login'),  
]