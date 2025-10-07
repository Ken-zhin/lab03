from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import UserRegistration
from .serializer import RegistrationSerializer

@api_view(['GET'])
def list_user(request):
    users = UserRegistration.objects.all()
    serializer = RegistrationSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)