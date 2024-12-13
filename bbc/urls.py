from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]