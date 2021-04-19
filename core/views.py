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
            select * from feedback
            ''',
            many=True
        )

        return Response({"message": "Success",
        "feed_back": feed_backs} ,status=status.HTTP_200_OK)
    
    except Exception as e:
        print(e)
        return Response({"message": "A server error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)