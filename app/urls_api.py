from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .apps import AppConfig
from .views import *

app_name = AppConfig.name

urlpatterns = format_suffix_patterns([
    re_path(r'^image/$', ImageUploadAPIView.as_view(), name='image_api'),
    re_path(r'^ocr/$', OcrAPIView.as_view(), name='ocr_api'),
    re_path(r'^history/$', HistoryListAPIView.as_view(), name='history_api'),
])
