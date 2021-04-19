from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 

from .models import *

from bus_tracker.utils import *


from django.contrib.auth.hashers import *
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def get_feedback(request):

    try:

        feed_backs = execute(
            '''
            select * from Feedback
            ''',
            many=True
        )

        return Response({"message": "Success",
        "feed_back": feed_backs} ,status=status.HTTP_200_OK)
    
    except Exception as e:
        print(e)
        return Response({"message": "A server error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def reply_email(request, *args, **kwargs):

    data = JSONParser().parse(request)
    print(data)

    msg_id = data.get('msg_id')
    email = data.get('email')
    title = data.get('title')
    message = data.get('message')

    if not (msg_id and email and title and message):
        return Response({"message": "Parameters missing"}, status=status.HTTP_400_BAD_REQUEST)

    try:

        # TODO send email using smtp api

        return Response({"message": "Successfully"} ,status=status.HTTP_200_OK)
        
    except Exception as e:
        print(e)
        return Response({"message": "A server error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)