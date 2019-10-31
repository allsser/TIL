from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('',views.index, name="index"),
    path('new/', views.new, name="new"),
    path('<int:students_pk>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('<int:students_pk>/edit/',views.edit, name="edit"),
    path('<int:students_pk>/update/',views.update, name="update"),
    path('<int:students_pk>/delete/',views.delete, name="delete")
]