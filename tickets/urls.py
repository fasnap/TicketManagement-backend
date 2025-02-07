# api/urls.py
from django.urls import path

from .views import TicketListCreateView, TicketDetailView

urlpatterns = [
    path('', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('<int:id>/', TicketDetailView.as_view(), name='ticket-detail'),

]