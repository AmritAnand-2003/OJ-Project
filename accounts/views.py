from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class UserRegisterView(APIView):
    # queryset = User.objects.all()
    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print("got a register hit")
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class UserLoginView(APIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    def post(self, request):
        # return Response(request.data, status= 201)
        print("got a login hit")
        print(request.data)
        breakpoint()
        serializer = UserLoginSerializer(data=request.data)
        print("serializer: ", serializer)
        if(serializer.is_valid()):
            print("serializer: ", serializer)
            print("serializer: ", serializer.data)
            print("it's valid")

            return Response(serializer.validated_data, status=201)
        return Response(serializer.errors, status=400)
        print("serializer: ", serializer)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=201)
