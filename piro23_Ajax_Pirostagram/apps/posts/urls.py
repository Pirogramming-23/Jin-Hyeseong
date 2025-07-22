from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_post, name='create_post'),
    path('like/<int:post_id>/', views.toggle_like, name='toggle_like'),
    path('comment/add/<int:post_id>/', views.add_comment, name='add_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]