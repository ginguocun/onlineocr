from rest_framework.generics import CreateAPIView, ListAPIView

from app.serializers import ImageUploadSerializer


class OcrAPIView(CreateAPIView):
    serializer_class = ImageUploadSerializer
