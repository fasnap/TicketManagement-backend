from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'status', 'id', 'user', 'username']
        read_only_fields = ['id', 'user', 'username']
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)