from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 

from .models import *
from .serializer import *

from django.contrib.auth.hashers import *
from rest_framework import status

from bus_tracker.utils import *

import datetime
from pytz import timezone

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
        return Response({"message": "Parameters missing"}, status=status.HTTP_400_BAD_REQUEST)

    try:

        driver = Driver.objects.create(
                    user_id=User.objects.get(id=user_id), 
                    name=name,
                    contact=contact,
                    password=make_password(password),
                    bus_id=Bus.objects.get(id=bus_id),
            )

        return Response({"message": "Driver Created Successfully"} ,status=status.HTTP_201_CREATED)
        
    except Exception as e:
        print(e)
        return Response({"message": "A server error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_driver(request):

    try:

        un_allocated = execute(
            '''SELECT id,bus_no FROM 
               Bus where id not in (select b.id from Bus as b left join Driver d on d.bus_id_id=b.id)''',
               many=True
        )


        alloc_driver = execute(
            '''select b.id,d.name,d.contact,b.bus_no from Driver as d left join Bus
         b on d.bus_id_id=b.id''',
         many=True
        )

        return Response({"message": "Success",
        "bus_data": un_allocated,"driver_list":alloc_driver} ,status=status.HTTP_200_OK)
    
    except Exception as e:
        print(e)
        return Response({"message": "A server error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
        return Response({"message": "A server error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def add_gps(request, *args, **kwargs):

    data = JSONParser().parse(request)
    print(data)

    token = data.get('token')
    lat = data.get('lat')
    lon = data.get('lon')

    status = 0
    if not (token and lat and lon):
        return Response({"message": "Parameters missing"}, status=status.HTTP_400_BAD_REQUEST)

    j_id = execute(
        '''
        select active_ride_j_id from driver where tokan=?
        ''',
        [token],
        many=True
    )

    if j_id == None or j_id == '':
        return Response({"message": "unauthorized user or inactive session"}, status=status.HTTP_400_BAD_REQUEST)

    else:
        # add location to location table
        # check if 1 minute passed since last update
        prev_time = datetime.datetime.now(timezone('Asia/Kolkata')) - datetime.timedelta(minutes=1)
        prev_time = str(prev_time)[:19]

        res = execute(
            '''SELECT  max(id) FROM 
               Location where j_id=%s''',j_id,
               many=False
        )
        if res[0] is None:
            # since first record
            status = 1
        else:
            res1 = execute(
            '''SELECT  id FROM 
               Location where id=%s and time(time) < time(%s)''',res[0],prev_time,
               many=False
        )
        if res is None:
            status = 0
        else:
            status = 1
        
        if status == 1:
            try:
                lat = float(lat)
                lon = float(lon)
                gps = lat,lon
                location = Location.objects.create(
                    gps=gps, 
                    j_id=j_id,
                )
                return Response({"message": "Adding Location"} ,status=status.HTTP_201_CREATED)

    
            except:
                print('incorrect gps input')
                return '0,0'
        # update gps table
        execute(
        '''
        update Journey set gps=?,last_update=? where id=?
        ''',
        [gps,get_date_full(),j_id],
        )
        return Response({"message": "Gps data added"} ,status=status.HTTP_200_OK)






