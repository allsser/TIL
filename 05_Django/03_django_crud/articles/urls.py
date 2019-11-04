from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    # path('',views.index, name="index"), # READ Logic - Index
    # path('new/',views.new, name='new'), # CREATE Logic - 사용자에게 폼 전달
    # path('create/',views.create, name='create'), # CREATE Logic - 데이터베이스에 저장
    # path('<int:article_pk>/', views.detail, name='detail'),  # READ Logic - Detail
    # path('<int:article_pk>/delete/', views.delete, name='delete'), # DELETE Logic
    # path('<int:article_pk>/edit/',views.edit, name='edit'),  # UPDATE Logic - 폼 전달
    # path('<int:article_pk>/update/', views.update, name='update'), # UPDATE Logic - DB 저장

    path('',views.index, name="index"), # READ Logic - Index
    path('create/',views.create, name='create'), # GET(new) / POST(create)
    path('<int:article_pk>/', views.detail, name='detail'),  # READ Logic - Detail
    path('<int:article_pk>/delete/', views.delete, name='delete'), # DELETE Logic
    path('<int:article_pk>/update/', views.update, name='update'), # FET(edit) / POST(update)
]