from django.shortcuts import render
# TODO 1226第五步.定义函数,用户访问指定url返回结果
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('欢迎访问index页面!')

# TODO 准备工作完毕,开启1225所学 --- HttpRequest对象类型 从setp1开始
# TODO 第一类:HttpRequest对象为GET请求中的url路径参数 如1/100 或 weather/beijing/2018/  是请求行发送的数据
# TODO Type1.定义模型函数
def book(request,cat_id,detail_id):  # 多两个参数,对应urls中的两个< > < >中内容
    # 视图函数中的参数名必须和path中的位置参数名一致
    print(f'用户访问的书大类地址是{cat_id},小类地址是{detail_id}')
    return HttpResponse('您访问的是具体书籍页面')
# 当浏览器输入127.0.0.1:8000/1/100/时,控制台打印---用户访问的书大类地址是1,小类地址是100
# 对应url设置见book.urls

# TODO 第二类:HttpRequest对象为GET请求中的Query String(查询字符串)  如:百度搜索 是请求行发送的数据
# TODO Type2. http://ip:port/url/?key=value&key2=value....中问号后面的就是查询字符串--key=value&key2=value....
def book2(request,cat_id,detail_id):  # 当浏览器访问http://127.0.0.1:8000/1/100/?a=10&b=20时↓
    query_string = request.GET  # GET大写,获取查询字符串中数据,变量接收
    print(query_string) # <QueryDict: {'a': ['10'], 'b': ['20']}>
    a=query_string['a']  # 获取QueryDict中键对应的值方式1
    b=query_string.get('b') # 获取QueryDict中键对应的值方式2
    print(f'查询字符串中第一个键a对应的值为{a},第二个键b对应的值为{b}')  # 10  20
    return HttpResponse('您访问地址加入了查询字符串') # 页面显示'您访问地址加入了查询字符串'

# TODO QueryDict对象
"""
QueryDict可以一键一值,也可以一键多值,如下
当我们访问http://127.0.0.1:8000/1/100/?a=10&b=20&a=666时
query_string = request.GET
print(query_string) 得到<QueryDict: {'a': ['10','666'], 'b': ['20']}>

一键一值情况:
1.常规获取其中的一键一值的值:
b = query_string.get('b')
print(b)  # 结果为 20
2.非常规操作:若一键一值,使用getlist获取,得到的是一个列表形式的值
b = query_string.getlist('b')
print(b)  # 结果为 ['20']
3.当键不存在时获取,假设为e,则默认返回None,也可自定义设置返回的值
e = query_string.get('e')
print(e) # 结果为None
e = query_string.get('e',798)
print(e) # 结果为798


一键多值情况:
1.常规获取其中的一键多值的值 -- 结果为列表形式返回: 
alist = query_string.getlist('a') 
print(alist)  # 结果为['10','666']
2.非常规操作:若一键多值,仍用get获取,则结果为获取到最后一个值:
a = query_string.get('a')
print(a) # 结果为 666
3.若查询的键不存在,则返回空列表 [],也可以设置默认值 getlist('键',默认值)

"""
# TODO 第三类:HttpRequest对象为POST请求的表单类型 Form Data  如:京东登录 是请求体body发送的数据
# 需使用postman软件进行POST形式的请求发送,使用前要设置settings → MIDDLEWARE中第四行middleware先注释掉,
# 否则用postman以POST方式发送请求时会显示403禁止访问
# TODO 定义模型函数,返回以POST请求访问页面时的返回数据  POST请求如form表单,json,xml
# TODO Type3. 用postman的POST--form data形式发送key:value数据username为ｗjma password为123456
def login(request):
    body = request.POST # 接收以POST请求发送的数据属性
    print(body)  #　结果是<QueryDict: {'username': ['wjma'], 'password': ['123456']}>
    return HttpResponse('您正在以POST请求方式访问页面')

# TODO 第四类：HttpRequest对象为POST请求的非表单类型 Non-Form 如:微博
# TODO Type4. 用postman发送jason数据 jason选raw
import json
def weibo(request):
    data = request.body  # body接收数据
    print(data)  # b'{\n\t"name":"zxm",\n\t"age":"18"\n\t\n}'二进制形式数据

    data_str = data.decode()  # 解码成字符串类型
    print(type(data_str), data_str)  # <class 'str'> jason形式的字符串类型
    # 得到的data_str  :   {"name":"zxm", "age":"18"}
    data_dict = json.loads(data_str) #　转换为字典形式
    print(data_dict)  # {'name': 'zxm', 'age': '18'}

    return HttpResponse('您正在以json形式访问weibo页面')
"""
发送数据格式:
{
    "name":"zxm",  # 必须双引号
    "age":"18"  # 最后一条数据后不能有都好
}
"""