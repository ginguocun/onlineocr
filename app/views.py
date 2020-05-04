from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from app.serializers import *


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return True  # To not perform the csrf check previously happening


class AppTokenObtainPairView(TokenObtainPairView):
    """
    Token Obtain API
    """
    serializer_class = AppTokenObtainPairSerializer


class ImageUploadAPIView(CreateAPIView):
    authentication_classes = (
        BasicAuthentication, CsrfExemptSessionAuthentication, SessionAuthentication, JWTAuthentication
    )
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageUploadSerializer


class OcrAPIView(APIView):
    """
    post:
    This is an API which can take an uploaded image(jpg, png) and find any letters in it.
    The request body should contain a File parameter called "image",
    and the size of the image file should be less than 2Mb.
    The result will be returned to user as JSON : ```{"content":[ 'Letter1', 'Letter2'...]}```
    """
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        image = request.data.get('image')
        record = ImageUpload.objects.create(image=image)
        letters = record.letters
        return Response({'content': letters}, status=200)


class HistoryListAPIView(ListAPIView):
    authentication_classes = (
        BasicAuthentication, CsrfExemptSessionAuthentication, SessionAuthentication, JWTAuthentication
    )
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageUploadSerializer
    queryset = ImageUpload.objects.all()
