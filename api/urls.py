from django.contrib import admin
from django.urls import path,include
from api import views
urlpatterns = [
    path('',views.sample, name='sample'),
    path('tasks/',views.TaskList,name='tasklist'),
    path('task/<int:pk>/',views.Task_ind,name='task'),
    path('task_fit',views.Task_fit,name='task_fit'),
]