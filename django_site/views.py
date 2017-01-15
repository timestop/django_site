# coding: utf-8

from django.http import HttpResponse

def hello(request):
    print request
    return HttpResponse('哈囉！！！！')

def add(request, a, b):
    print request
    sum = int(a) + int(b)
    return HttpResponse('sum of {0} and {1} is {2}'.format(a, b, sum))

def match(request, a, b):
    print request
    a = float(a)
    b = float(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    html = '''
            <html>
                sum = {s}<br>
                dif = {d}<br>
                pro = {p}<br>
                quo = {q}<br>
            </html>
           '''.format(s=s, d=d, p=p, q=q)
    return HttpResponse(html)
