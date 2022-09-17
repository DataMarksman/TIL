from django.urls import path
from . import views

# app_name을 설정한 이후로는 url 태그에서 콜론(:)앞에 반드시 명시해줘야함
app_name = 'accounts'
# 요 뒤에 name => 이건 url 태그에서 하드코딩 하지 않고 쓰기 위한것
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
]
