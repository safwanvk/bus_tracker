from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 

from .models import *
from .serializer import *


from django.contrib.auth.hashers import *
from rest_framework import status
import random
import string

# Create your views here.
@api_view(['POST'])
def create_kid(request, *args, **kwargs):

    data = JSONParser().parse(request)
    print(data)

    parent_name = data.get('parent_name')
    kid_name = data.get('kid_name')
    email = data.get('email')
    kid_section = data.get('kid_section')
    bus = data.get('bus')

    if not (parent_name and kid_name and email and kid_section):
        return Response({"message": "Parameters missing"}, status=400)

    try:
        # auto_pass = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
        # p_id = Parent.objects.get_or_create(name=parent_name, email=email, password=make_password(auto_pass))
        
        # Kid.objects.create(
        #     name=kid_name,
        #     section=kid_section,
        #     parent_id=Parent.objects.get(id=p_id),
        #     bus_id=Bus.objects.get(id=bus)
        # )

        all_parent_kid = Parent.objects.raw(
            '''
            select k.id as kid_id,p.id,k.name as kid_name,p.name as parent_name,
            p.contact,p.email,b.id as bus_id,b.bus_no from Parent as p left join Kid k on p.id=k.parent_id_id left join Bus b on k.bus_id_id=b.id
            '''
        )

        all_parent_kid_serializer = ParentSerializer(all_parent_kid, many=True)
        return Response({"message": "Kid Created Successfully",'parent':all_parent_kid_serializer.data} ,status=200)

    except Exception as e:
        print(e)
        return Response({"message": "A server error occurred"}, status=500)