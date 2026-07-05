import django_filters
from .models import Todo
from django.utils import timezone

class TodoFilter(django_filters.FilterSet):
    is_overdue = django_filters.BooleanFilter(method='filter_is_overdue')
    
    class Meta:
        model = Todo
        fields = {
            'title': ['icontains'],
            'description': ['icontains'],
            'status': ['exact'],
            'is_archived': ['exact'],
        }

    def filter_is_overdue(self, queryset, name, value):
        today = timezone.now()
        finished_statuses = [Todo.Status.COMPLETED, Todo.Status.CANCELLED]
        if value: #is overdue true
            return queryset.filter(due_datetime__lt=today).exclude(status__in=finished_statuses)
        return queryset.filter(due_datetime__gte=today) | queryset.filter(status__in=finished_statuses)