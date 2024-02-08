from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class CoreAction(models.Model):
    created_by = models.ForeignKey(User, related_name="%(class)s_created_by", related_query_name="%(class)s_created_by", 
                                   on_delete=models.SET_NULL, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name="%(class)s_updated_by", related_query_name="%(class)s_updated_by", 
                                        on_delete=models.SET_NULL, null=True, blank=True, default=None)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta: abstract = True

class TaskDetails(CoreAction):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]
    title          = models.CharField(max_length=100)
    description    = models.TextField()
    due_date       = models.DateField()
    priority       = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=LOW)
    is_complete    = models.BooleanField(default=False)

    class Meta:
        db_table            = "task_details"

    def __str__(self):
        return self.title
