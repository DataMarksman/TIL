from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('details/', views.details, name='details')

]