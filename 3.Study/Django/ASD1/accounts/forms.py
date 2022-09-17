from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# 생각해보면 여기는 AuthenticationForm이랑 PasswordChangeForm은 등장하지 않음 => 이건 쟝고 내부에서(빌트인 form) 직접 가져옴
# 이곳은 유저의 생성과 변경과 관련된 부분은 커스텀이 많이 필요하기 때문에 직접 상속받아 만드는 쪽이라 forms.py에 쓰임.


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = User 하고 싶었는데, Django는 User 클래스를 직접 가져와서 참조하는게 아니고 (models.py 에서 import 해오는게 아니고)
        # django.contrib.auth 여기서 현재 프로젝트에 내가 활성화해둔 사용자 모델을 참조해야 한다고 쟝고는 권장 (이후 심화 쟝고 파트에서 부연설명)
        model = get_user_model()
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 원래 필드가 되게 많으니까 수정하고자 하는 필드를 작성해둠
        fields = (
            'email',
            'first_name',
            'last_name',
        )
