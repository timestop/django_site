# coding: utf-8

# from django.http import HttpResponse
# from django.template.loader import get_template
# from django import template
from django.shortcuts import render_to_response

def hello(request):
    print request
    return HttpResponse('哈囉！！！！')

def add(request, a, b):
    print request
    sum = int(a) + int(b)
    return HttpResponse('sum of {0} and {1} is {2}'.format(a, b, sum))

def math(request, a, b):
    print request
    a = float(a)
    b = float(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b

    # t = get_template('math.html')
    # c = template.Context({'s': s, 'd': d, 'p': p, 'q': q})
    # return HttpResponse(t.render(c))
    local_dict = locals()
    print local_dict

    return render_to_response('math.html', locals())

def menu(request):
    foods = [
    {
        'name': '蒜泥白肉',
        'price': 120,
        'comment': '好吃喔',
        'is_spicy': True
    },
    {
        'name': '京都排骨',
        'price': 130,
        'comment': '酸酸甜甜 der',
        'is_sour': True,
        'is_sweet': True
    },
    {
        'name': '雞腿飯',
        'price': 140,
        'comment': '又油又香',
        'is_sweet': True
    },
    {
        'name': '紅油抄手',
        'price': 50,
        'comment': '辣辣辣 der',
        'is_spicy': True
    },
    {
        'name': '苦瓜湯',
        'price': 50,
        'comment': '苦苦 der QQ',
        'is_bitter': True
    }]
    return render_to_response('menu.html', locals())
