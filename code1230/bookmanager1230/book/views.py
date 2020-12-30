from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
    return HttpResponse('初始环境搭建后测试')

# TODO 1.类视图  -- 相比面向过程可读性好、复用性高
# 面向过程方式 判断用户不同请求方式GET\POST 返回不同页面
def index(request):
    print(request.method)
    if request.method == 'GET':
        return HttpResponse('当前用户通过GET方式访问index页面')
    else:
        return HttpResponse('当前用户通过POST方式访问index页面')
# 面向对象方式 通过类视图继承View,url中定义的类调用父类as_view方法，从而dispatch实现路由分发 可读性好，提升复用性，
from django.views import View
class JDlogin(View):
    def get(self,request):
        return HttpResponse('当前用户通过GET方式访问JDlogin页面')
    def post(self,request):
        # return self.aaa(request)  执行此行的话 就无法执行下行 只能执行一个return
        return HttpResponse('当前用户通过POST方式访问JDlogin页面')
    def aaa(self):
        return HttpResponse('无法实现，因父类中http_method_names不含aaa,只能通过含有的名字并在此处定义的函数内部去调用实现')
# 后接urls中定义path  path('Center/',JDlogin.as_view())

# TODO 2.类视图多继承，重写dispatch -- 用户点击我的订单，判断用户是否登录，若未登录则跳转到登录页面 访问页面跳转到accounts/login页面404报错
class Ifelse_checkorders(View):
    def get(self,request):
        islogin = True
        if islogin:
            return HttpResponse('已登录，可查看订单')
        else:
            return HttpResponse('应跳转到请登录页面')
    def post(self,request):
        islogin = False
        if islogin:
            return HttpResponse('已登录，可查看订单')
        else:
            return HttpResponse('应跳转到请登录页面')
# 此种单继承方法，每个请求函数中都要重复写if else 麻烦 使用多继承 ↓
from django.contrib.auth.mixins import LoginRequiredMixin
class Check_orders(LoginRequiredMixin, View):
    def get(self,request):
        return HttpResponse('若已登录，显示此页面')
    def post(self,request):
        return HttpResponse('若已登录，显示此页面')

# TODO 3.中间件  -- 处理请求和响应伴随发生的  -- 新建middleware.py写入
