from django.contrib import admin
from .models import Review  # models.py에서 만든 모델 import

admin.site.register(Review)  # 관리자 페이지에 등록
