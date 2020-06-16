from django.contrib import admin
from .models import Project, Bug


# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = (
        'reported_by',
        'date_created',
        'date_updated',
        'project',
        'severity',
        'assigned_user'
    )

    readonly_fields = ('date_created', 'date_updated')
    fieldsets = (
        (None, {'fields': (
            'reported_by',
            'date_created',
            'date_updated',
            'project',
            'severity',
            'description',
            'assigned_user'
        )}),
    )
    search_fields = (
        'severity',
        'project__name',
        'reported_by__email',
        'assigned_user__email',
        'date_created'
    )
    ordering = ('date_created', 'project__name')