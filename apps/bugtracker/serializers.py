from rest_framework import serializers
from .models import Bug, Project, ProjectUsers

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
            'id',
            'name'
        )

class AssignedSerializer(serializers.ModelSerializer):
    project_name = serializers.StringRelatedField(source='project')
    user_name = serializers.StringRelatedField(source='user')

    class Meta:
        model = ProjectUsers
        fields = (
            'project',
            'user',
            'project_name',
            'user_name'
        )