from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('index页面')

def book(request,cat_id,detail_id,c_id):
    print(f'访问地址url中第一层为{cat_id},第二层为{detail_id},第三层为{c_id}')
    return HttpResponse('book页面')

def book2(request,cat_id,detail_id):
    query_string = request.GET
    print(query_string)  # <QueryDict: {'a': ['10'], 'b': ['20'], 'c': ['30', '40']}>
    a = query_string.get('a')
    print(a)  # 55
    b = query_string['b']
    print(b)  # 66
    c = query_string.getlist('c')
    print(c)  # ['77', '88']
    d = query_string.getlist('d',666)
    print(d)  # 666
    return HttpResponse('book2页面')

def login(request):
    body_data = request.POST
    print(body_data)  #　<QueryDict: {'name': ['哈哈'], 'sss': ['呵呵']}>
    return HttpResponse('Login页面')

import json
def weibo(request):
    b_data = request.body
    print(b_data)  # b'{\n\t"name":"zxm",\n\t"age":"18"\n\t\n}'
    str_data = b_data.decode()
    print(str_data)
    # {
    #     "name": "zxm",
    #     "age": "18"
    #
    # }
    data = json.loads(str_data)
    print(data)  # {'name': 'zxm', 'age': '18'}
    return HttpResponse('weibo界面')