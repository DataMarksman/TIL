from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('JJangjunho/', include('JJangjunho.urls')),
    path('accounts/', include('accounts.urls')),
]
