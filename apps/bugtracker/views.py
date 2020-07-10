from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework_tracking.mixins import LoggingMixin
from .models import Bug, Project, ProjectUsers, User
from .serializers import BugSerializer, ProjectSerializer, AssignedSerializer
from rest_framework.response import Response
# Create your views here.

class BugListView(generics.ListAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

class AttributesListView(generics.GenericAPIView):
    permission_classes = (
        permissions.AllowAny,
    )      
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "response": [
                    {"severities": Bug.BUG_SEVERITY_CHOICES},
                    {"statuses": Bug.BUG_STATUS_CHOICES},
                    {"operating systems": Bug.BUG_OS_CHOICES}
                ]
            },
            status=status.HTTP_200_OK
        ) 

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

class AssignedListView(generics.ListAPIView):
    queryset = ProjectUsers.objects.all()
    serializer_class = AssignedSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    
    def get_queryset(self):
        
        self.queryset = ProjectUsers.objects.filter(project__id=self.kwargs['project_id'])
        
        return self.queryset
    


        