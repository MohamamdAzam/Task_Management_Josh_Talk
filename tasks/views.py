from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Task, User
from .serializers import TaskSerializer, AssignTaskSerializer, UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class AssignTaskView(APIView):
    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            user_ids = request.data.get("assigned_users", [])

       
            users = User.objects.filter(id__in=user_ids)
            if len(users) != len(user_ids):
                return Response({"error": "One or more user IDs are invalid."}, status=status.HTTP_400_BAD_REQUEST)

            task.assigned_users.set(users)
            task.save()
            return Response({"message": "Users assigned successfully."}, status=status.HTTP_200_OK)
        
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)


class UserTasksView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            tasks = user.tasks.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
