from django.urls import path
from . import views


app_name = 'auth_system'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('forgot_password/',views.forgot_password,name='forgot_password')
]