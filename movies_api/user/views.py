from rest_framework import status
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from user.serializer import RegisterUserSerializer
from rest_framework.views import APIView
from user.utils import get_token
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from .redis import redis_instance



class UserRegistrationApiView(APIView):
    # User registration

    def post(self , request ,*args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            reg_object = serializer.save()
            if reg_object:
                token= get_token(request.data,request)
                return Response({
                    'access_token': token,
                }, status=status.HTTP_201_CREATED)
        error_details={}
        a=0
        for key , value in serializer.errors.items():
            error_details[str(a)]=str(value[0])
            a=a+1
        return Response(
            {
                'errors': error_details
            }, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        if username and password:
            user = authenticate(username=username, password=password)
            print(user, 'user')
            if user:
                auth_login(request, user)
                token = get_token(request.data, request)
                return Response(
                    {
                        'access_token': token,
                    },
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    {
                        'message': 'Invalid credentials.',
                        'data': {}
                    },
                    status=status.HTTP_401_UNAUTHORIZED)

class RequestCountView(APIView):
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        count = 0
        count = redis_instance.get('counter')
        return Response(data={'requests': int(count)})


class RequestCountResetView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        count = redis_instance.set('counter', 0)
        return Response(data={'message': 'request counter reset successfully'})