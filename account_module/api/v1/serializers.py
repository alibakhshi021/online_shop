from rest_framework import serializers
from ...models import User, Profile
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
import random
import string
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "password1",
        ]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError({"detail": "password dos not match "})

        try:
            validate_password(attrs.get("password"))

        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"detail": list(e.messages)})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password1")
        email = validated_data["email"]
        password = validated_data["password"]
        random_username = "user_" + "".join(
            random.choices(string.ascii_lowercase + string.digits, k=8)
        )

        user = User.objects.create_user(
            email=email, username=random_username, password=password
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_date = super().validate(attrs)
        validated_date["email"] = self.user.email
        validated_date["user_id"] = self.user.pk
        return validated_date


class ChangePassApiSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get("new_password") != attrs.get("confirm_password"):
            raise serializers.ValidationError({"detail": "password dos not match "})

        try:
            validate_password(attrs.get("new_password"))

        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})
        return super().validate(attrs)


class ProfileApiSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "first_name", "last_name", "description", "email"]
        read_only_fields = ["email"]


class ActivationResendSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "dos not exists"})
        if user_obj.is_verified:
            raise serializers.ValidationError(
                {"detail": "user is already activate and verified"}
            )
        attrs["user"] = user_obj
        return super().validate(attrs)
