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
        # print(serializer.data,'+++++++++++++++++')

        serializer.save()
        user_data = serializer.data
        user = CustomUser.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        print(current_site,relative_link)
        port = request.get_port()
        absurl = 'http://'+ current_site + ":" + port + relative_link + "?token="+str(token)
        print(absurl) 

        email_body = "Hi " + user.username +' Use link below to verify your email \n'+ absurl
        data = {'email_body': email_body,'email_subject':"verify your email",'to_email': user.email}
        Util.send_email(data)

        return Response(user_data,status=status.HTTP_201_CREATED)
    

class VerifyEmail(generics.GenericAPIView):
    serializer_class = VerifyEmailSerializer

    def get(self, request):
        token = request.GET.get('token')
        print(token,'token+++++++++++')
        # payload = jwt.decode(token, settings.SECRET_KEY,algorithms=['HS256'])
        # print(payload,'++++++++++')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms= ['HS256'])

            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Activation link has expired'}, status=status.HTTP_400_BAD_REQUEST)

        except jwt.exceptions.DecodeError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        
        except jwt.exceptions.InvalidSignatureError:
            return Response({'error': 'Signature verification failed'}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

