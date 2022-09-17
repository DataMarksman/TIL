from django.contrib.auth.models import AbstractUser

# 장고는 시작부터 유저모델을 대체하는 것을 권장하고 있음.
# 나중에 커스텀 할 여지를 남겨두기 위해서 pass로!
class User(AbstractUser):
    pass
