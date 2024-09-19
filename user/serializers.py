from rest_framework import serializers
from .models import CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=69,min_length=3,write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email','username','password']

    def validate(self,attrs):
        email = attrs.get('email','')
        username = attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError("The username should only contain alpha numeric characters.")
        
        return attrs
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    

class VerifyEmailSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = CustomUser
        fields = ['token']

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=68,write_only=True)
    username = serializers.CharField(read_only=True,max_length=30)
    tokens = serializers.CharField(read_only=True,max_length=66)

    class Meta:
        model = CustomUser
        fields = ['email','password','username','tokens']

    def validate(self,attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')

        user = auth.authenticate(email=email,password=password)
        # if not user.is_active:
        #     raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
        if not user:
            raise AuthenticationFailed('Invalid credentials Try again.')
        
        return {
            'email':user.email, 'username':user.username,'tokens':user.tokens      }
        return super().validate(attrs)

