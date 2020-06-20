from rest_framework import serializers
from .models import Bug

class BugSerializer(serializers.ModelSerializer):

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