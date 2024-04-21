from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from .serializers import HousesSerializers
from accounts.serializers import MessageSerializer
from .models import Houses

# Create your views here.
class HouseAPIView(APIView):
    """
    Handles All House Processes
    """


    def get (self, request, *args , **kwargs):
        """
        get all houses in the database
        """
        houses = Houses.objects.all()
        serializer = HousesSerializers(houses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # def post(self, request, *args, **kwargs):
    #     """
    #     Used to get a house by id
    #     """
    #     house_id = request.data.get("house_id")
    #     house = Houses.objects.get(id=house_id)

    #     # sent house id doesn't exist
    #     if not house:
    #         message = {"message": "House Doesn't Exist"}
    #         serializer = MessageSerializer(message)
    #         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
    #     serializer = HousesSerializers(house)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetHouseAPIView(RetrieveAPIView):
    pass