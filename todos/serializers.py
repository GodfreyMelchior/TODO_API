from rest_framework import serializers
from datetime import date
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """Serializer for the Todo model, converting model instances to JSON and vice versa.
    """
    is_overdue = serializers.SerializerMethodField()
    is_completed = serializers.SerializerMethodField()
    
    def get_is_overdue(self, obj):
        return obj.is_overdue
    
    def get_is_completed(self, obj):
        return obj.is_completed

    def validate_due_date(self, value): 
        """Custom validation for the due_date field to ensure it is not in the past during create.
        """
        # if self.instance is None and  value < date.today(): #prevent setting due date in the past during creation
        #     raise serializers.ValidationError("Due date cannot be in the past.")
        # return value   

        if value < date.today(): #prevent setting due date in the past during creation and update 
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value 

    def validate_title(self, value):
        """Custom validation for the title field to ensure it is not empty during update and create.
        """
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty or just a white space.")
        return value    

    def create(self, validated_data):
        """Create a new Todo instance with the validated data and the todo is not archived during creation.
        """
        validated_data.pop('is_archived', None)  # Remove is_archived from validated_data to prevent setting it during creation
        return Todo.objects.create(**validated_data)     

    class Meta:
        model = Todo
        fields = [
            'id', 'title', 'description', 'status',
            'is_archived', 'created_at', 'due_date',
            'is_overdue', 'is_completed'
        ]  # Include some additional fields for read-only purposes
        read_only_fields = ['is_overdue', 'is_completed', 'created_at']