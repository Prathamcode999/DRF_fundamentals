#you can create serializer wherever you want 

from rest_framework import serializers
from .models import Blog, Comment

class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class blogSerializer(serializers.ModelSerializer):
    comments_serializer = commentSerializer(many = True, read_only = True) #comments_serializer is a variable which is taken from models,passed in realted_name 
    class Meta:
        model = Blog
        fields = '__all__'
    