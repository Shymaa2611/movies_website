from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
   path('login/',auth_view.LoginView.as_view(template_name='login.html'), name='login'),
   path('signup/',views.signUp.as_view(), name='signup'),
]
