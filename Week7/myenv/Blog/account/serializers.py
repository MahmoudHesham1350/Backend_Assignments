#pip install django-restframework
#pip install environs

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length = 8,read_only=True)
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 150)
    password = serializers.CharField(min_length =8,max_length =128,write_only=True)

    def validate(self,data):
        username = data.get('username','').strip()
        password = data.get('password')

        return data
    

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self,data):
        self.token = data.get('refresh')
        return data
    
    def save(self,**kwargs):
        try:
            RefreshToken(self.token).blacklist()  #converts the token string into a token object -- then blacklist it
        except:
            pass

class AccountDetails(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        