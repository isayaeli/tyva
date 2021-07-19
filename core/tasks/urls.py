from django.urls import path
from .views import addTask, update_task, assign_task
urlpatterns = [
    path('new-task', addTask, name='add_task'),
    path('update-task/<int:id>/', update_task, name='update_task'),
    path('assing-task', assign_task, name='assign_task')
]