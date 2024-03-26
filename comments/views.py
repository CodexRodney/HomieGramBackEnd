from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CommentsSerializers
from accounts.serializers import MessageSerializer

# Create your views here.
class CommentsApi(APIView):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        """
        Used to post a comment about houses
        """
        data = {
            "house_id" : request.data.get("house_id"),
            "user_id" : request.data.get("user_id"),
            "comment" : request.data.get("comment"),
        }

        # checking data sent if any required field is missing return 400
        if not all(data):
            message ={"message": "Missing Some required Fields"}
            serializer = MessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
        # checking for nested sockets
        if request.data.get("nested") and not request.data.get("nested_id"):
            # no nested id provided
            message ={"message": "Missing Nested ID For Nested Post"}
            serializer = MessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        # appending nested id and nested to data
        data["nested"] = request.data.get("nested")
        data["nested_id"] = request.data.get("nested_id")

        serializer = CommentsSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'message': "Successfully Posted",
                }
            serializer = MessageSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
