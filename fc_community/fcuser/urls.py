from django.urls import path
from . import views #함수 가져오기

urlpatterns = [
    #register 등록 
    path('register/', views.register),
    path('login/', views.login), #로그인 기능
]
