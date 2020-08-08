from rest_framework import serializers
from .models import Bug, Project, ProjectUsers

class BugSerializer(serializers.ModelSerializer):
    reported_by_name = serializers.StringRelatedField(source='reported_by', read_only=True)
    class Meta:
        model = Bug
        fields = (
            'reported_by',
            'reported_by_name',
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

    def create(self, validated_data):
        validated_data['reported_by'] = self.context['request'].user
        return super().create(validated_data)

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