from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializers import *


class ImageUploadAPIView(CreateAPIView):
    serializer_class = ImageUploadSerializer


class OcrAPIView(APIView):

    def post(self, request):
        image = request.data.get('image')
        record = ImageUpload.objects.create(image=image)
        letters = record.letters
        return Response({'content': letters}, status=200)


class HistoryListAPIView(ListAPIView):
    serializer_class = ImageUploadSerializer
    queryset = ImageUpload.objects.all()
