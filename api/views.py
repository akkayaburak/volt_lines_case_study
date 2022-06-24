from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import passenger
from api.serializers import PassengersSerializer

class PassengerApiView(APIView):
# 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        passengers = passenger.objects
        serializer = PassengersSerializer(passengers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'name': request.data.get('name'), 
            'surname': request.data.get('surname'), 
            'email': request.data.get('email'),
            'status' : request.data.get('status'),
            'phone_number' : request.data.get('phone_number')
        }
        serializer = PassengersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
