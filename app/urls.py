from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('update/<str:pk>', views.update_task, name="update"),
    path('delete/<str:pk>', views.delete_task, name="delete"),
]