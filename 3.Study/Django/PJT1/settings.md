# Django Crud with Auth

## Project 시작하기 & Settings

> 💡 Django 기본 세팅 명령어들

```bash
# 가상환경을 설정합니다. 뒤의 venv는 다른 이름으로 설정할 수 있습니다.
# gitignore.io에 가서 python, django, venv를 기입한 후 .gitignore파일 생성 후 복사 + 붙여넣기
$ python -m venv venv

# 가상환경을 활성화합니다. 이후 pip list 명령어를 통해 초기화를 확인합니다.
$ source venv/Scripts/activate

# 관련 패키지들을 다운받습니다.
$ pip install django==3.2.13

# 패키지 설치가 완료된 경우 requirements.txt를 갱신하여 관리합니다.
$ pip freeze > requirements.txt

# 만약 requirements.txt가 있는 경우?
$ pip install -r requirements.txt

# 프로젝트를 만들어야 하는 경우 + 현재 디렉토리에 폴더구조 잡기
$ django-admin startproject <프로젝트 명> .

# 프로젝트 중간에 참여하는 경우 migrate 진행
# 설계도를 작성합니다.
$ python manage.py makemigrations
# 설계도를 DB에 반영합니다.
$ python manage.py migrate 
# 설계도 반영 여부 보기
$ python manage.py showmigrations
# migration의 SQL문 보기
$ python manage.py sqlmigrate articles 0001

# 프로젝트 시작 명령어 + 현재 위치에서(.) => manage.py가 생기게 됩니다.
$ django-admin startproject <프로젝트명> .

# app 생성 => 이후 settings.py의 installed apps에 등록합니다.
# 이 때, trailing comma(,)를 빼먹지 않도록 주의합니다. 
$ python manage.py startapp <앱 이름>
```



> 프로젝트 시작 전 유저 대체 먼저하기

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```

```python
# accounts models.py
from django.contrib.auth.models import AbstractUser

# 장고는 시작부터 유저모델을 대체하는 것을 권장하고 있음.
# 나중에 커스텀 할 여지를 남겨두기 위해서 pass로!
class User(AbstractUser):
    pass
```



> Template 구조 잡기 & Namespace

```python
# settings.py

TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
    },
]
```

* 이후 최상단(manage.py가 있는곳)에 templates 폴더를 만들고 그 안에 base.html을 생성합니다. 

* 상속받을 템플릿들이 들어있는 폴더는 다음과 같이 구조화합니다.

```
<앱 이름>/
	templates/
		<앱 이름>
			상속받을.html
```





