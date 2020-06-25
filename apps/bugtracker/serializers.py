from rest_framework import serializers
from .models import Bug, Project

class BugSerializer(serializers.ModelSerializer):
    reported_by = serializers.StringRelatedField()
    class Meta:
        model = Bug
        fields = (
            'reported_by',
            'date_created',
            'date_updated',
            'project',
            'operating_system',
            'severity',
            'status',
            'title',
            'description',
            'assigned_user'
        )

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = (
            'name',
        )