from django.urls import path
from . import views

# 이제 템플릿 없고 이 링크를 사용자에게 직접 제공할 필요가 X
# 그래서 지금은 app_name 굳이 쓸 필요 X
# 지금은 json data로 가공하기 위한 과정만 필요하기 때문에..
urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
]
