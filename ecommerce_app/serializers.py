from rest_framework import serializers
from .models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name' ,'last_name','email' ,'password')
    
    def create(self,validated_data):
        user = User.objects.create_user(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email= validated_data['email'],
            password= validated_data['password'],
        )

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name' ,'last_name','email','is_staff')
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id','name','description']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


