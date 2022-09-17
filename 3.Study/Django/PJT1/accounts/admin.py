from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# 얘도 내가 만든 User 커스텀 클래스기때문에 등록해줘야 admin 사이트에서 보인다.
admin.site.register(User, UserAdmin)
