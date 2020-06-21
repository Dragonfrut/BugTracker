from django.urls import path
from . import views


urlpatterns = [
    path('bugs', views.BugListView.as_view(), name='bug-list'),
    path('bugs/attributes', views.AttributesListView.as_view(), name='attributes-list')
    
]
