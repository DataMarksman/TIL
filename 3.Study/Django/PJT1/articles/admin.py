from django.contrib import admin
from .models import Article  # 가지고 와야 쓸 수 있음.

# admin site에 테이블을 보고, 실제로 views.py에 crud 관련 로직을 작성하지 않은 상태에서도,
# admin site에 등록되고 난 이후는 간단하게 데이터 변경을 할 수 있는 기능을 장고가 이미 제공하고 있으니 등록하는것.
admin.site.register(Article)
