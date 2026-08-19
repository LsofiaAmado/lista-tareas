from django.shortcuts import render

from rest_framework import generics
from .models import Tarea
from .serializers import TareaSerializer


class TareaListCreateView(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer


class TareaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer