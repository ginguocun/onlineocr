from rest_framework import serializers

from app.models import ImageUpload


class ImageUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageUpload
        fields = '__all__'
