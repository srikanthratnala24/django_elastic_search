from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer, VerifyEmailSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings

class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data= user)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        user_data = serializer.data
        user = CustomUser.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token
        current_site = request.get_host()
        relative_link = reverse('email-verify')
        absurl = 'http://'+ current_site + relative_link + "?token="+str(token) 

        email_body = "Hi " + user.username +' Use link below to verify your email \n'+ absurl
        data = {'email_body': email_body,'email_subject':"verify your email",'to_email': user.email}
        Util.send_email(data)

        return Response(user_data,status=status.HTTP_201_CREATED)
    

class VerifyEmail(generics.GenericAPIView):
    serializer_class = VerifyEmailSerializer

    def get(self,request):
        token = request.GET.get('token')

        try:

            payload = jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'],options={"verify_signature": False})
            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_verified == True:
                user.is_verified = True
                user.save()
                return Response({'email': 'successfully activated' }, status=status.HTTP_200_OK)

    
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation expired' }, status=status.HTTP_400_BAD_REQUEST)

        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'invalid token' }, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
