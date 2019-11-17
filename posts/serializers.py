from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 
                  'username',
                   'email']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 
                  'suite', 
                  'city', 
                  'zipcode']

class ProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    
    class Meta:
        model = Profile
        fields = ['pk', 
                  'name', 
                  'email', 
                  'address']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['pk', 
                  'userId', 
                  'title', 
                  'body']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 
                  'postId', 
                  'name', 
                  'email', 
                  'body']

class ProfilePostSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['pk', 
                  'name', 
                  'email', 
                  'address', 
                  'posts']

class PostCommentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['userId',
                  'title', 
                  'body',
                  'comments']