from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.select_related('user').prefetch_related('tags').filter(
            user=self.request.user  # Solo tareas del usuario logueado
        )