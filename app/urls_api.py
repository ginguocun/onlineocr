from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .apps import AppConfig
from .views import OcrAPIView

app_name = AppConfig.name

urlpatterns = format_suffix_patterns([
    re_path(r'^ocr/$', OcrAPIView.as_view(), name='ocr_api'),
])
