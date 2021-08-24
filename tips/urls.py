from django.urls import path
from . import views

urlpatterns = [
    path('', views.tips, name='tips'),
    path('view/', views.view_tips, name='view_tips'),
]
