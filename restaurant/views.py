from django.shortcuts import render

from django.http import HttpResponse
from .models import Menu
from .serializers import MenuSerializers, BookingSerializer 
from rest_framework import generics
from rest_framework import viewsets
from .models import Booking
from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, 'index.html')


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
