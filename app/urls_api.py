from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from .apps import AppConfig
from .views import *

app_name = AppConfig.name

urlpatterns = format_suffix_patterns([
    re_path(r'^token_obtain_pair/$', token_obtain_pair, name='token_obtain_pair'),
    re_path(r'^token_refresh/$', token_refresh, name='token_refresh'),
    re_path(r'^ocr/$', OcrAPIView.as_view(), name='ocr_api'),
    re_path(r'^history/$', HistoryListAPIView.as_view(), name='history_api'),
])
