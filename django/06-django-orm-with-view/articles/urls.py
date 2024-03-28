from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    # <> 안에 변수 넣음 된다
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # 삭제와 수정은 조회가 먼저 되어야 함(= pk가 필요)
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
