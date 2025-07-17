from django.urls import path
from .views import *

app_name = 'devtools'

urlpatterns = [
    path('devtools/', devtool_list, name='devtool_list'),
    path('devtools/<int:pk>', devtool_detail, name='devtool_detail'),
    path('devtools/create/', devtool_create, name='devtool_create'),
    path('devtools/<int:pk>/update/', devtool_update, name='devtool_update'),
    path('devtools/<int:pk>/delete/', devtool_delete, name='devtool_delete'),
]
