from django.shortcuts import render
from rest_framework import generics,viewsets, permissions
from .models import Booking, Menu
from .serializers import UserSerializer,MenuSerializer,BookingSerializer
from django.contrib.auth.models import User



#Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    #permission_classes = [permissions.IsAuthenticated] 

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    #permission_classes = [permissions.IsAuthenticated] 

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 

# class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    #permission_classes = [permissions.IsAuthenticated] 