from django.db import models
from apps.user.models import User

# Create your models here.

#Project Data Model
class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#ProjectUsers is a bridge between project and user
class ProjectUsers(models.Model):
    project = models.ForeignKey(
        Project,
        db_index=True,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    user = models.ForeignKey(
        User,
        db_index=True,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

      
    def __str__(self):
        return ''
    
    #fixes a pluralization issue and forces project and user to be unique together
    class Meta:
        unique_together = (
            ('project', 'user'),
        )
        verbose_name_plural = 'Project Users'


#Bug Data Model
class Bug(models.Model):
    #Constants for severity dropdown
    BUG_SEVERITY_MILD = 'mild'
    BUG_SEVERITY_MEDIUM = 'meduim'
    BUG_SEVERITY_HOT = 'hot'
    #Constants for bug status
    BUG_STATUS_OPEN ='open'
    BUG_STATUS_PENDING = 'pending'
    BUG_STATUS_RESOLVED = 'resolved'
    BUG_STATUS_CLOSED = 'closed'

    #Creates a list of lists
    BUG_SEVERITY_CHOICES = (
        (BUG_SEVERITY_MILD, 'Mild'),
        (BUG_SEVERITY_MEDIUM, 'Medium'),
        (BUG_SEVERITY_HOT, 'Hot')
    )

    BUG_STATUS_CHOICES = (
        (BUG_STATUS_OPEN, 'Open'),
        (BUG_STATUS_PENDING, 'Pending'),
        (BUG_STATUS_RESOLVED, 'Resolved'),
        (BUG_STATUS_CLOSED, 'Closed')
    )

    #the user that created the bug
    reported_by = models.ForeignKey(
        User,
        db_index=True,
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )

    #current date/time of created bug & time of an update
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    #the severity dropdown with defaulted mild
    severity = models.CharField(
        default = BUG_SEVERITY_MILD,
        choices = BUG_SEVERITY_CHOICES,
        max_length = 6
    )
    
    #the status dropdown with default open
    status = models.CharField(
        default = BUG_STATUS_OPEN,
        choices = BUG_STATUS_CHOICES,
        max_length = 8
    )

    title = models.TextField(default = '')
    description = models.TextField()

    #Operating system

    #the project that the bug is attached to
    project = models.ForeignKey(
        Project,
        db_index=True,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    #user who has been assigned (can be blank)
    assigned_user = models.ForeignKey(
        User,
        related_name='bugs', 
        db_index=True,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

