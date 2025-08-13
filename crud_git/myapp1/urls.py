
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_data/', views.add_data, name='add_data'),
    path('edit_data/<int:id>', views.edit_data, name='edit_data'),
    path('delete_data/<int:id>', views.delete_data, name='delete_data'),
]
