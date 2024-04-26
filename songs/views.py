from django.shortcuts import render
from .models import song
from .serializers import SongSerializer, Userserializer
from rest_framework import generics
from rest_framework.filters import SearchFilter

from django.contrib.auth.models import User


from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

class SongListCreateView(generics.ListCreateAPIView):
    queryset = song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [SearchFilter]
    filterset_fields = ['genre', 'historical_period', 'author', 'location']
    search_fields = ['title', 'author', 'genre', 'historical_period', 'location']
    permission_classes = [IsAuthenticated]

class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    
    
#usser creation view 
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [AllowAny]

class SongUpdateView(generics.UpdateAPIView):
    queryset = song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
