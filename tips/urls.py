from django.urls import path
from . import views

urlpatterns = [
    path('', views.tips, name='tips'),
    path('view/', views.view_tips, name='view_tips'),
    path('add/', views.add_tip, name='add_tip'),
    path('edit/<int:tip_id>/', views.edit_tip, name='edit_tip'),
    path('delete/<int:tip_id>/', views.delete_tip, name='delete_tip'),
]
