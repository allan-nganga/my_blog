from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),    # Homepage URL
    path('post/new/', views.new_post, name='new_post'), # Add a new post URL
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'), # Delete post URL
]