from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import (
    require_http_methods,  # 여러개의 요청을 허용하는 데코레이터
    require_POST,
    require_safe,
)
from .models import Article  # 가져와야 쓸 수 있음
from .forms import ArticleForm


@require_safe  # require_GET 대신 권장하는 데코레이터, 단순 전체 조회이므로 GET 요청을 받아줌.
def index(request):
    articles = (
        Article.objects.all()
    )  # objects 매니저가 데이터베이스에서 Article 테이블의 레코드 전체를 쿼리셋으로 가져와줌
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# is valid 메서드는 유효성 검사를 진행한 다음 그 결괏값을 True 혹은 False로 반환함.
@login_required  # 로그인이 되어있는 유저만 게시글을 작성할 수 있어야 함.
# 만약 데커레이터에서 블록당해 튕겨버리게 되면 settings.py에 설정된 LOGIN_URL의 주소로 가게되는데,
# 별다른 설정을 해두지 않았다면 기본값은 accounts/login으로 가게 되므로 앱 이름을 애초에 accounts 라고 해둔것
@require_http_methods(['GET', 'POST'])  # 게시글 작성은 기본적으로
def create(request):
    if request.method == 'POST':
        form = ArticleForm(
            request.POST
        )  # create에서 form으로 넘어온 객체가 POST 방식은 request.POST에 담기게 됨.
        if form.is_valid():
            article = form.save()  # 유효성 검증이 끝난 경우는 데이터베이스에 저장됨.
            return redirect('articles:detail', article.pk)  # redirect는 Get 방식.
    else:
        form = ArticleForm()
    # print(form.errors) => is valid의 반환값이 False인 경우, 유효성 검증 실패 원인을 딕셔버리로 형태로 만들어줌
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)  # 특정 레코드를 가져온 후에
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)  # 바로 context 인자로 넣어줌


# 그럼 이런데선 왜 login_required 안쓰냐? => 데커레이터 튕기는건 GET 방식이어서 POST 데이터가 소실되는데,
# POST 요청만 받는 함수같은 경우는 함수 is_authenticated로 해야함.
# 1. article 디테일 페이지에서 로그인 안하고 삭제하려고 하니까
# 2. article delete 함수에 만약 login_required가 있었다? 그러면 accounts/login으로 로그인 하라고 보낼것
# 3. accounts 로그인 함수 도착해서 로그인 하니까 redirect(request.GET.get('next') or 'articles:index') 이게 있어가지고
# 4. next 파라미터로 다시 delete로 왔을텐데 그시점에서는 post 데이터가 날아가 있을거니까.
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)  # 뭔지 가져오고
        article.delete()  # 그걸 delete 한다.
    return redirect('articles:index')  # 이후 메인페이지로 리다이렉트


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)  # 어쨌든 update도 하나를 찍어서 가져와야 함 (뭘 수정하는지 알아야 하니까)
    if request.method == 'POST':
        # Create a form to edit an existing Article,
        # but use POST data to populate the form.
        # data 옵션이 첫번 째 인자인데, instance는 좀 뒤에 있어서 명시해서 넣어주느라 앞에 instance= 이부분이 붙음
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect(
                'articles:detail', article.pk
            )  # 리다이렉트 시 인자도 같이 넘기고 싶은 경우 이렇게 콤마 뒤에 붙임
    else:
        # Creating a form to change an existing article.
        form = ArticleForm(instance=article)
    # 해당 인덴팅 레벨은 is_valid가 실패했을 경우의 예외처리 로직
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
