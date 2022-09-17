from django import forms
from .models import Article

# 원래는 input 태그로 사용자 정보를 직접 받았지만, 이후 is_valid() 유효성 검증을 위해 사용함.
# 기본적으로 모델폼을 상속받아 데이터베이스에 저장할 form을 쉽게 생성하도록 도움
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        # CSS 부분은 widget을 이용해서 커스텀
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                # 이건 유효성 검사랑은 별 관련이 없고 html 태그의 attribute를 설정하는것. 실제로 개발자도구에서 우회할 수 있음.
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        # Textarea를 구현하기 위한 위젯
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={'required': 'Please enter your content'},
    )

    class Meta:  # Meta? 데이터를 위한 데이터
        model = Article
        fields = '__all__'  # 리스트나 튜플로도 표현할 수 있음.
        # exclude로 제외하는 것을 선택할 수 있음.
        # exclude = ('title',)  => 하나짜리인 경우 튜플은 원소 오른쪽에 , 콤마를 꼭 찍어줘야함.
