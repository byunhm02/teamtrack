from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('kakao/login',views.kakao_login),
    path('kakao/register',views.kakao_register),
    #path('kakao/logout',views.kakao_logout),
    #path('google/login',views.google_login),
    #path('google/register',views.google_register),
    path('login',views.login),
    path('register',views.register),
    path('verify', views.verify, name='verify'),
]