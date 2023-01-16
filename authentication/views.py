from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.

class AuthView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={'msg':'hello auth'},status=status.HTTP_200_OK)

class UserCreateView(generics.GenericAPIView):
    serializer_class =UserCreationSerializer
    def post(self,request):
        data = request.data
        serializers = self.serializer_class(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)

        return Response(data=serializers.errors,status=status.HTTP_400_BAD_REQUEST)

