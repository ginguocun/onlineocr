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


class RegisterAPIView(GenericAPIView):
    """
    post:
    This is an API for user registration.
    """
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user_model = get_user_model()
        user_model.objects.create_user(**data)
        return Response({'msg': 'OK'}, status=status.HTTP_200_OK)


class OcrAPIView(GenericAPIView):
    """
    post:
    This is an API which can take an uploaded image(jpg, png) and find any letters in it.
    """
    authentication_classes = (
        BasicAuthentication, CsrfExemptSessionAuthentication, JWTAuthentication
    )
    permission_classes = ()
    serializer_class = OcrSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        # update the created_by if the user is is already logged in
        user = self.request.user
        if user:
            if user.id:
                data['created_by_id'] = user.id
        record = ImageUpload.objects.create(**data)
        letters = record.letters
        return Response({'content': letters}, status=status.HTTP_200_OK)


class HistoryListAPIView(ListAPIView):
    """
    get:
    This is an API used to obtain the historical upload records.
    """
    authentication_classes = (
        BasicAuthentication, CsrfExemptSessionAuthentication, JWTAuthentication
    )
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageUploadSerializer
    queryset = ImageUpload.objects.all()

    def get_queryset(self):
        self.queryset = super().get_queryset()
        # only staffs can view all of the records, otherwise can only view their own uploads.
        if not self.request.user.is_staff:
            self.queryset = self.queryset.filter(created_by_id=self.request.user.id)
        return self.queryset
