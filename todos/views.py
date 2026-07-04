from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from .filters import TodoFilter

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    filterset_class = TodoFilter

    def get_queryset(self):
        if self.action == 'list':
            return Todo.objects.all() # Return only non-archived todos for the list action
        return Todo.all_objects.all()     # Return all todos for other actions