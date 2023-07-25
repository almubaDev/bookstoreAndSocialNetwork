from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from .forms.forms import EmailAuthenticationForm
from .views import *

app_name = 'user_manager'

urlpatterns = [
    # path('', mostrarUsuarios, name='mostrarUsuarios'),
    path('signUp/', signUp, name='signUp'),
    path('signUp/successful/', successfulRegistration, name='successfulRegistration'),
    path('login/', auth_views.LoginView.as_view(authentication_form= EmailAuthenticationForm, template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]


