from django.shortcuts import render

# Create your views here.
# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import ShahihBukharis
from .serializers import ShahihBukharisSerializer

class ShahihBukhariListApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the ShahihBukharis items for given requested user
        '''
        shahih_bukharis = ShahihBukharis.objects.all()[:10]
        serializer = ShahihBukharisSerializer(shahih_bukharis, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'kitab': request.data.get('kitab'), 
            'terjemah': request.data.get('terjemah'), 
            'arab': request.data.get('arab')
        }
        serializer = ShahihBukharisSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    