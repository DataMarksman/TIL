from django.shortcuts import render

def dinner(request, menu, number):
    context = {
        'food' : menu,
        'people': number,
    }
    return render(request, 'dinner.html', context)