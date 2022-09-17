from django.urls import path
from . import views

app_name = 'JJangjunho'
urlpatterns = [
    path('', views.index, name = 'index')
]
