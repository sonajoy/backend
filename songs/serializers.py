from rest_framework import serializers
from .models import song
from django.contrib.auth.models import User

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = song
        fields = '__all__'

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =['id','username','email','password']
        extra_kwargs = {"password": {"write_only": True}}
         
         
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


#creaate a file 