from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 

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

        # reg = Attendance.objects.create(
        #             sid=Student.objects.get(sid=std_id), 
        #             arrival=arrival,
        #             event_id=Event.objects.get(event_id=event_uid),
        #     )

        return Response({"message": "Successfully signed in"} ,status=200)