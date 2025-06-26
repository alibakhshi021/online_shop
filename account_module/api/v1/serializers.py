from rest_framework import serializers
from ...models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
import random
import string



class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only= True )
    password = serializers.CharField(max_length=255, write_only= True )
    
    class Meta:
        model = User
        fields = ['email', 'password', 'password1']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError({'detail': 'password dos not match '})
        
        try:
            validate_password(attrs.get('password'))

        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'detail': list(e.messages)})    
        return attrs


    def create(self, validated_data):
        validated_data.pop('password1')
        email = validated_data['email']
        password = validated_data['password']
        random_username = "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

        user = User.objects.create_user(
            email=email,
            username=random_username,
            password=password
        )
        return user

