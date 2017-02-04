# coding: utf-8

from django.http import HttpResponse
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
