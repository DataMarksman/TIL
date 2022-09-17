from django.shortcuts import render, redirect
from django.contrib.auth import (
    login as auth_login,
)  # 기본 view 함수가 login으로 되어있기때문에 재귀함수를 피하기 위해 alias 설정
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm

# is valid 메서드는 유효성 검사를 진행한 다음 그 결괏값을 True 혹은 False로 반환함.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)s
        if form.is_valid():
            auth_login(request, form.get_user())  # 재귀함수가 되지 않도록 사용한 auth_login 함수
            # form.get_user() ?? => AuthenticationForm의 인스턴스인 form 객체의 메서드중 하나인데, 유효성 검사를 통과했다면 user를 반환함.
            # 함수 의 인자 자리의 단축평가를 이용해, request.GET에 다음 주소에 대한 정보가 있으면 그쪽으로 가고, 아니면 전체페이지로 이동
            # 여기서 request.GET 뒤에 있는 get는 진짜 딕셔너리에서 키값 찾는 그 메서드
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)  # 첫 번째 인자는 request
    return redirect('articles:index')


# 회원가입은 CustomUserCreationForm 활용함
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        # CustomUserChangeForm이랑 인자 갯수가 다르다는거 유의
        # 만들때는 그냥 만들어도 되는데?
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        # 수정할땐 누구꺼를 수정해야 하는지 알아야 하기 때문에
        form = CustomUserChangeForm(request.POST, instance=request.user)
        # form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    # 비밀번호는 기존 값을 불러와서 변경하는게 아니라 그냥 새로 파게 됨
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # 인자 위치가 좀 정해져 있는 편이라 명시안하고 넣어도 됨
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    # 나중에 이녀석이 context로 넘어간 부분의 하단에 Raw passwords are not stored, so there is no way to see this user's password,
    # but you can change password using 'this form' 이라는 문구에서 마지막 this form 링크를 클릭하면 자동적으로 accounts/password 주소로 보내는데,
    # 이런 것 때문에 애초에 앱 이름을 accounts로 해둠
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
