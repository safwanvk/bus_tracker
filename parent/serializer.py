from rest_framework import serializers

from .models import *

class KidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = Kid
        fields =[
            'id',
            'name'
            ]



class ParentSerializer(serializers.HyperlinkedModelSerializer):
    kid = KidSerializer(source='id')

    class Meta:
        model = Parent
        fields = [
            'id',
            'name',
            'email',
            'contact',
            'kid']

