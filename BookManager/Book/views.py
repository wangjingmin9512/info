from django.shortcuts import render
# TODO 视图 1.导模块
from django.http import HttpResponse
from django.http import HttpRequest
# Create your views here.
# TODO 视图 2.定义函数
def index222(request):
    return HttpResponse('欢迎来到index页面!')