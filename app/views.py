from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from app.serializers import *


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return True  # To not perform the csrf check previously happening


class OcrAPIView(GenericAPIView):
    """
    post:
    This is an API which can take an uploaded image(jpg, png) and find any letters in it.
    """
    authentication_classes = (
        BasicAuthentication, CsrfExemptSessionAuthentication, SessionAuthentication, JWTAuthentication
    )
    permission_classes = ()
    serializer_class = OcrSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        # update created_by if user is login
        user = self.request.user
        if user:
            if user.id:
                data['created_by_id'] = user.id
        record = ImageUpload.objects.create(**data)
        letters = record.letters
        return Response({'content': letters}, status=status.HTTP_200_OK)


class HistoryListAPIView(ListAPIView):
    authentication_classes = (
        BasicAuthentication, CsrfExemptSessionAuthentication, SessionAuthentication, JWTAuthentication
    )
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageUploadSerializer
    queryset = ImageUpload.objects.all()

    def get_queryset(self):
        self.queryset = super().get_queryset()
        if not self.request.user.is_staff:
            self.queryset = self.queryset.filter(created_by_id=self.request.user.id)
        return self.queryset
