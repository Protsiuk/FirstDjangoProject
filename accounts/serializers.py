from rest_framework import serializers
from accounts.models import User

from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password =serializers.CharField(min_length=6)


    def validate(self, attrs):
        email =attrs.get("email")
        password = attrs.get("password")

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Sorry, invalid credentials.")

        attrs["user"] = user
        return attrs
