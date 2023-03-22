from django.urls import path
from . import views
# app_name='bankaccount'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('form/',views.form,name='form'),
    path('detail/',views.detail,name='detail'),


]