from django.urls import path
from . import views

urlpatterns = [
    # 'http://localhost/pages/'라는 경로로 요청했을 경우
    path('',views.intro),
    # 'http://localhost/pages/throw/'라는 경로로 요청했을 경우
    path('throw/',views.throw),
    path('catch/',views.catch),
    path('art/',views.art),
    path('result/',views.result),
    path('user_new/',views.user_new),
    path('user_create/',views.uesr_create),
    path('static_sample/',views.static_sample),
    path('index/',views.index),
    # 
]
