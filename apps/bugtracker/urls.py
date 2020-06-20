from django.urls import path
from . import views


urlpatterns = [
    path('bugs', views.BugListView.as_view(), name='bug-list')
]
