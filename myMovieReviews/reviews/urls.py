from django.urls import path
from .views import *

urlpatterns = [
    path('', reviews_list, name="reviews_list"),
    path('<int:pk>/', reviews_detail, name='reviews_detail'),
    path('<int:pk>/delete/', reviews_delete, name='reviews_delete'),
    path('<int:pk>/edit/', reviews_edit, name="reviews_edit"),
    path('create/', reviews_create, name='reviews_create'),
]