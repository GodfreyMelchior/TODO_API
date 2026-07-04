from django.db import models
from datetime import date

# Create your models here.

class TodoManager(models.Manager):
    """Custom manager for Todo model that filters out archived todos by default.
    """
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=False) #filtering out archived todos
class Todo(models.Model):
    """Todo model representing a task with status and due date.
    """
    class Status(models.TextChoices): #choices for todo status
        PENDING = 'PENDING', 'Pending'
        COMPLETED = 'COMPLETED', 'Completed'
        CANCELLED = 'CANCELLED', 'Cancelled'
        ON_HOLD = 'ON_HOLD', 'On Hold'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        IN_REVIEW = 'IN_REVIEW', 'In Review'

    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.PENDING,
    )
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=date.today)
    objects = TodoManager() #default manager excluding archived todos
    all_objects = models.Manager() #default manager including archived todos

    @property
    def is_overdue(self):
        finished_statuses = [self.Status.COMPLETED, self.Status.CANCELLED]
        return self.due_date < date.today() and self.status not in finished_statuses

    @property
    def is_completed(self):
        return self.status == self.Status.COMPLETED

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

    