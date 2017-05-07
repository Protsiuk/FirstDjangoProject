from rest_framework import serializers
from publications.models import Publication
from accounts.serializers import UserSerializer


class PublicationSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField("get_author_details")
    hello = serializers.SerializerMethodField("get_hello_world")


    def get_hello_world(self, obj):
        return "Hello World"


    def get_author_details(self, obj):
        return UserSerializer(obj.author).data


    class Meta:
        model = Publication
        fields = ("title", "body", "author")
        # fields = ("__all__") for all fiels


class CreatePublicationSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()