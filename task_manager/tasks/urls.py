from . import views
from django.urls import path

urlpatterns = [
    path('', views.home , name="home_page"),
    path('new-task/', views.new_Task , name="new-task"),
    path('edit-task/<int:id>', views.edit_task , name="edit-task"),
    path('task-completed/<int:id>/', views.switch_completed , name="task-completed"),
    path('delete-task/<int:id>/', views.delete_task , name="delete-task"),
]