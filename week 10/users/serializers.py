from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}  # Ensure email is required
        }
        
    def validate_email(self, value):
        """Check if email is already in use."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    
    def validate(self, data):
        """Use Django's built-in password validation."""
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Run Django's password validation rules
        try:
            validate_password(data['password'])
        except ValidationError as e:
            raise serializers.ValidationError({"password": e.messages})

        return data

    def create(self, validated_data):
        """Use Django's create_user() method to apply hashing and validation."""
        validated_data.pop('password2')  # Remove password2 before saving
        user = User.objects.create_user(**validated_data)
        return user

