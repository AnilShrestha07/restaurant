from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.handle_register, name='register'),
    path('login/', views.handle_login, name='login'),
    
    

]