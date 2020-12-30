from django.shortcuts import render

# Create your views here.
# TODO 1.面向过程 实现判断用户请求方式get\post返回不同页面
from django.http import HttpResponse
def if_else_checkpage(request):
    print(request.method)  # request.method获取请求方式 GET或POST
    if request.method == 'GET':
        return HttpResponse('请求方式为get')
    else:
        return HttpResponse('请求方式为post')

# TODO 2.类视图 实现如上功能
from django.views import View
class Check_request(View):
    def get(self,request):
        return HttpResponse('请求方式为get')
    def post(self,request):
        return HttpResponse('请求方式为post')

# TODO 3.类视图多继承 LoginRequiredMixin 1.导包 2.多继承
from django.contrib.auth.mixins import LoginRequiredMixin
class Check_orders(LoginRequiredMixin,View):
    def get(self,request):
        return HttpResponse('若已登录，返回此页面')
    def post(self,request):
        return HttpResponse('若已登录，返回此页面')
# http://127.0.0.1:8000/accounts/login/?next=/check3/

# TODO 4.中间件 -- middleware.py
