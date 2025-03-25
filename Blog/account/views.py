from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model,authenticate # to get the user model and user authentication
from rest_framework.permissions import AllowAny,IsAuthenticated #for the permission classes
from .serializers import RegisterSerializer,LoginSerializer,LogoutSerializer,AccountDetails
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

User = get_user_model()

class RegisterForm(CreateAPIView):
    queryset = User
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginForm (APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        
        serializer = LoginSerializer(data = request.data)
        
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        

        user = None
        user = authenticate(username=username,password = password)

        if not user:
            return Response({"Error" : "Invalid Credentials"},status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)  # to refresh the JWT token
        return Response({"user":{"id":user.id,"username":user.username,"email":user.email},"refresh":str(refresh),"access":str(refresh.access_token)},status=status.HTTP_200_OK)


class LogoutForm(APIView):
    def post(self,request):
        serializer = LogoutSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response({"Message":"the User logged out successfully"},status=status.HTTP_200_OK)

# every user can get his account details
class Account(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        account = User.objects.get(pk=request.user.pk)
        serializer = AccountDetails(account)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
            

