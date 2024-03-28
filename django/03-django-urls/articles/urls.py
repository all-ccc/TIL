from django.urls import path
# 명시적 상대경로
from . import views     # 현재 위치에서 views를 import 하겠다

app_name = 'articles'   # 이거하면 articles가 name에 태그로 붙음
urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('greeting/<str:name>/', views.greeting, name='greeting'),
    path('articles/<int:num>/', views.detail, name='detail'),
]
