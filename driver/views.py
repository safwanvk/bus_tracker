from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 

from .models import *

from django.contrib.auth.hashers import *

# Create your views here.
@api_view(['POST'])
def create_driver(request, *args, **kwargs):

    data = JSONParser().parse(request)
    print(data)

    user_id = data.get('user_id')
    bus_id = data.get('bus')
    name = data.get('name')
    contact = data.get('contact')
    password = data.get('password')

    if not (user_id and bus_id and name and contact and password):
        return Response({"message": "Parameters missing"}, status=400)

    try:

        driver = Driver.objects.create(
                    user_id=User.objects.get(id=user_id), 
                    name=name,
                    contact=contact,
                    password=make_password(password),
                    bus_id=Bus.objects.get(id=bus_id),
            )

        return Response({"message": "Driver Created Successfully"} ,status=200)
        
    except Exception as e:
        print(e)
        return Response({"message": "A server error occurred"}, status=500)