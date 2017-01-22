# coding: utf-8

# from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

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
