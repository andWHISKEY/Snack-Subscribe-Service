from django.contrib import admin
from django.urls import path
import main.views

urlpatterns = [
    path('',main.views.home, name='home'),
    path('recommend/',main.views.recommend, name='recommend'),
    path('subscribe/',main.views.subscribe, name='subscribe'),
    path('shopping/',main.views.shopping, name='shopping'),
    path('payment/',main.views.payment,name='payment'),
    path('mypage/',main.views.mypage,name='mypage'),
    path('result/',main.views.result, name='result'),
]
