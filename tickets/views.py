from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import TicketSerializer
from .models import Ticket
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TicketListCreateView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self, request):
        user=request.user
        if user.is_superuser:
            tickets=Ticket.objects.all()
        else:
            tickets=Ticket.objects.filter(user=user)
        serializer=TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=TicketSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)