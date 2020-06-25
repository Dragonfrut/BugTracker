from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework_tracking.mixins import LoggingMixin
from .models import Bug, Project
from .serializers import BugSerializer, ProjectSerializer
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



        