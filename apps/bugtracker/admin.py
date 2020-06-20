from django.contrib import admin
from apps.user.models import User
from .models import Project, Bug, ProjectUsers



# Register your models here.

class ProjectUsersInline(admin.TabularInline):
    model = ProjectUsers
    verbose_name_plural = 'Project Users'
    classes = ['collapse']
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [ProjectUsersInline]


'''
the clunky way
@admin.register(ProjectUsers)
class ProjectUsersAdmin(admin.ModelAdmin):
    list_display = ('project', 'user')
'''


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = (
        'reported_by',
        'date_created',
        'date_updated',
        'project',
        'title',
        'severity',
        'status',
        'assigned_user'
    )

    readonly_fields = ('date_created', 'date_updated')
    fieldsets = (
        (None, {'fields': (
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
        )}),
    )
    search_fields = (
        'severity',
        'title',
        'status',
        'project__name',
        'reported_by__email',
        'assigned_user__email',
        'date_created'
    )
    ordering = ('date_created', 'project__name', 'status')
    list_filter = ('status', 'severity')

    #gets the bug form
    def get_form(self, request, obj=None, **kwargs):
        self.obj = obj
        return super(BugAdmin, self).get_form(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        #limit options to the parent assessment
        #looks specifically for assigned user
        if db_field.name == "assigned_user" and self.obj:
            kwargs["queryset"] = (
                #filters for only users that are in the project the bug is in
                User.objects.filter(
                    id__in=ProjectUsers.objects.filter(
                        project=self.obj.project
                    ).values('user__id')
                )
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
