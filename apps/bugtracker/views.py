from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework_tracking.mixins import LoggingMixin
from .models import Bug
from .serializers import BugSerializer
# Create your views here.

class BugListView(generics.ListAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )