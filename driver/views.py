from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 

from .models import *
from .serializer import *

from django.contrib.auth.hashers import *
from rest_framework import status

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

        un_allocated = Bus.objects.raw("""SELECT id,bus_no FROM 
               Bus where id not in (select b.id from Bus as b left join Driver d on d.bus_id_id=b.id)""")

        un_allocated_serializer = BusSerializer(un_allocated, many=True)

        alloc_driver = Bus.objects.raw("""select b.id,d.user_id_id,d.name,d.contact from Bus as b left join Driver
         d on d.bus_id_id=b.id""")

        alloc_driver_serializer = BusSerializer(alloc_driver, many=True)

        return Response({"message": "Driver Created Successfully",
        "bus_data": un_allocated_serializer.data,"driver_list":alloc_driver_serializer.data} ,status=200)
        
    except Exception as e:
        print(e)
        return Response({"message": "A server error occurred"}, status=500)

# delete driver
@api_view(['DELETE'])
def delete_driver(request, pk):

    try:

        try: 
            driver = Driver.objects.get(id=pk) 
        except Driver.DoesNotExist: 
            return Response({'message': 'The Driver does not exist'}, status=status.HTTP_404_NOT_FOUND) 

        driver.delete() 
        return Response({'message': 'Driver was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    except Exception as e:
        print(e)
        return Response({"message": "A server error occurred"}, status=500)