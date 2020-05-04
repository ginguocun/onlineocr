from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from app.models import ImageUpload


class AppTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(AppTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token


class ImageUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageUpload
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': True}
        }
