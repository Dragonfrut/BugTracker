from django.urls import path
from . import views


urlpatterns = [
    path('bugs/<int:bug_id>', views.BugRetrieveUpdateDeleteView.as_view(), name='bug'),
    path('bugs', views.BugListView.as_view(), name='bug-list'),
    path('bugs/attributes', views.AttributesListView.as_view(), name='attributes-list'),
    path('projects', views.ProjectListView.as_view(), name='project-list'),
    path('assigned/<int:project_id>', views.AssignedListView.as_view(), name='assigned-list')
    
]
