from rest_framework import serializers
from publications.models import Publication
from accounts.serializers import UserSerializer


class PublicationSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField("get_author_details")
    def get_author_details(self, obj):
        return UserSerializer(obj.author).data


    class Meta:
        model = Publication
        fields = ("title", "body", "author")
