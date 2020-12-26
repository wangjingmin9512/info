from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('当前访问index页面为普通ip:port/url页面')

def book(request,cat_id,detail_id,c_id):
    """
    HttpRequest第一类:url 如1/100
    视图函数定义的后两个参数分别一一对应path中的路径
    """
    # 访问网址为 http://127.0.0.1:8000/1/100/555
    print(f'访问地址url中第一层为{cat_id},第二层为{detail_id},第三层为{c_id}')
    # TODO 访问地址url中第一层为1,第二层为100,第三层为555
    return HttpResponse('当前访问book页面为GET类型URL')

def book2(request,cat_id,detail_id):
    """
    第二类:GET查询字符串
    """
    # http://ip:port/url/?key=value&key2=value2...
    # http://127.0.0.1:8000/2/200/?a=10&b=20&c=30&c=40
    query_string = request.GET
    print(query_string)  # <QueryDict: {'a': ['10'], 'b': ['20'], 'c': ['30', '40']}>
    a = query_string.get('a')
    print(a)  # 10
    b = query_string['b']
    print(b)  # 20
    c = query_string.getlist('c')
    print(c)  # ['30', '40']
    d = query_string.getlist('d',99999)
    print(d)  # 99999
    # 若getlist查询没有,返回空列表[] get没有 返回默认为None
    # 若getlist查单个,返回列表单个数据如['20'],get查多个,返回最后一个值如50
    return HttpResponse('当前访问book2页面为GET类型查询字符串')

def login(request):
    body_data = request.POST
    print(body_data)  #　<QueryDict: {'name': ['梅花'], 'gender': ['未知']}>
    # 使用postman模拟表单发送,需注释掉settings中MIDDLEWARE的第四行
    return HttpResponse('当前访问Login页面为POST类型请求体发送的表单类型')

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
    return HttpResponse('POST非表单形式访问weibo界面')