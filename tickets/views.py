from functools import partial
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import TicketSerializer
from .models import Ticket
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

# Create your views here.
class TicketListCreateView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self, request):
        user=request.user
        if user.is_superuser:
            tickets=Ticket.objects.all()
        else:
            tickets=Ticket.objects.filter(user=user)
        status_filter=request.query_params.get('status')
        priority_filter=request.query_params.get('priority')
        user_filter=request.query_params.get('user')
        
        if status_filter:
            tickets = tickets.filter(status__iexact=status_filter)
        
        if priority_filter:
            tickets = tickets.filter(priority__iexact=priority_filter)
        
        if user_filter and user.is_superuser:
            tickets = tickets.filter(
                Q(user__username__icontains=user_filter) |
                Q(user__email__icontains=user_filter)
            )
        serializer=TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=TicketSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketDetailView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get_object(self, id, user):
        if user.is_superuser:
            return get_object_or_404(Ticket, id=id)
        else:
            return get_object_or_404(Ticket, id=id, user=user)

    def get(self, request, id):
        user=request.user
        ticket=self.get_object(id, user)
        serializer=TicketSerializer(ticket)
        return Response(serializer.data)
    
    def put(self, request, id):
        user=request.user
        ticket=self.get_object(id, user)
        if ticket.status == 'resolved' and not user.is_superuser:
            return Response(
                {'error': 'Cannot edit resolved tickets'}, 
                status=status.HTTP_403_FORBIDDEN
            )
            
        serializer=TicketSerializer(ticket, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        user=request.user
        ticket=self.get_object(id, user)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)