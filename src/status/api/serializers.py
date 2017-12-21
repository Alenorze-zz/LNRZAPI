from rest_framework import serializers

from status.models import Status
from accounts.api.serializers import UserPublicSerializer


class CustomSerializer(serializers.ModelSerializer):
    content = serializers.CharField()
    email   = serializers.EmailField()
    

class StatusSerializer(serializers.ModelSerializer):
    uri  = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    class Meta: 
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data

    def get_uri(self, obj):
        return "/api/users/{id}/".format(id=obj.id)
    