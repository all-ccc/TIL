from django.urls import path
# 명시적 상대경로
from . import views     # 현재 위치에서 views를 import 하겠다

app_name = 'pages'
urlpatterns = [
    # path('index/', views.index),
]