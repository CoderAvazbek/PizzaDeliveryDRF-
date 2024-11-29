from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.

class HelloOrdersView(generics.GenericAPIView):
    def get(self, request):
        message = {
            "message": "Hello Orders"
        }
        return Response(message, status=status.HTTP_200_OK)
