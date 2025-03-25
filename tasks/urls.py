from django.urls import path
from .views import CreateTaskView, AssignTaskView, UserTasksView, CreateUserView

urlpatterns = [
    path('tasks/create/', CreateTaskView.as_view(), name='create-task'),
    path('tasks/<int:task_id>/assign/', AssignTaskView.as_view(), name='assign-task'),
    path('users/<int:user_id>/tasks/', UserTasksView.as_view(), name='user-tasks'),
    path('users/create/', CreateUserView.as_view(), name='create-user'),
]

