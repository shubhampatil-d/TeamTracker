# core/api_views.py

from rest_framework import generics, permissions
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

class ProjectListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save(
            organization=self.request.user.organization,
            created_by=self.request.user
        )

class TaskListCreateAPI(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(project__organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save()
