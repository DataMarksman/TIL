from django.shortcuts import render
import random

lotto = ['실패']*10 + ["성공"]

count = 0
count_t = 0
hp_t = 100
price = 0
# Create your views here.
def index(request):
    global count
    count += 1
    print(f'인덱스 대리에 {count}번 도달 했어요?!')
    nums = [i for i in range(11)]
    
    pick = random.choice(nums)
    
    context = {
        'lotto' : lotto[pick],
        'count' : int(count),
        'name' : 'kyou',
        'foods' : ['피자','나라','치킨','공주','야'],
        'address' : {
            'city': 'seoul'
        } 
    }
    
    return render(request, 'index.html', context)

def throw(request):
    global count_t
    global hp_t
    count_t += 1
    print(f'Throw 과장님은 {count_t}번 고통 받았어요!')
    
    nums = [i for i in range(11)]
    pick = random.choice(nums)
    hp_t -= pick
    context = {
        'name' : 'kyou',
        'count' : int(count_t),
        'random': int(pick),
        'last_hp' : int(hp_t),
        
    }
    
    return render(request, 'throw.html', context)

def catch(request):
    print('catch에 도달했다.')
    print('================')
    
    print(request)
    print(type(request))
    print(request.GET.get('message'))
    
    context = {
        'myMessage' : request.GET.get('message')
    }
    
    return render(request, 'catch.html', context)


def greeting(request, age, word):
    result = False
    if word == word[::-1]:
        result = True
    
    context = {
        'word': word,
        'result': result,
        'name' : 'kyou',
        'age' : age,
    }
    
    return render(request, 'greeting.html', context)