from rest_framework.permissions import IsAuthenticated

class TaskListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    # ... resto del código ...