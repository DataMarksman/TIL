from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # print('인덱스 대리에 도달했다!!')
    nums = [1, 5, 7, 2, 3, 4, 6]
    foods = ['피자', '치킨', '햄버거']

    pick = random.choice(nums)
    context = {
        'name' : 'alex',
        'foods': foods,
        'address': {
            'city': 'seoul'
        },
        'pick': pick
    }

    return render(request, 'index.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # print('catch에 도달했다')
    # print('================')
    # print(request)
    # print(type(request))
    # print(request.GET)
    # print(request.GET.get('message'))

    context = {
        'myMessage': request.GET.get('message')
    }

    return render(request, 'catch.html', context)

def greeting(request, age, word):
    result = False
    if word == word[::-1]:
        result = True

    context = {
        'age': age,
        'result': result,
        'word': word,
    }
    return render(request, 'greeting.html', context)
