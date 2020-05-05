from django.contrib.auth import get_user_model
from rest_framework import serializers

from app.models import ImageUpload


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']


class ImageUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageUpload
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': True}
        }


class OcrSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True, help_text='A image file, the size should be less than 2Mb')

