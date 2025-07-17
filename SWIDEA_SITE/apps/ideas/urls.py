from django.urls import path
from .views import *

app_name = 'ideas'

urlpatterns = [
    path('', idea_list, name='idea_list'),
    path('toggle_star/', toggle_star, name='toggle_star'),
    path('adjust_interest/', adjust_interest, name='adjust_interest'),
    path('create/', idea_create, name='idea_create'),
    path('ideas/<int:pk>/', idea_detail, name='idea_detail'),
    path('ideas/delete/<int:pk>/', idea_delete, name='idea_delete'),
    path('ideas/update/<int:pk>/', idea_update, name='idea_update'),
]
