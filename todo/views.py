from django.shortcuts import render

from .models import Todo
from .serializer import TodoSerializer

from rest_framework import routers, serializers, viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer