from django.urls import path
from . import views  # 현재 디렉토리 위치에서 views.py를 불러옴

# app_name을 설정한 이후로는 url 태그에서 콜론(:)앞에 반드시 명시해줘야함
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
]
