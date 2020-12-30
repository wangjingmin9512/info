from django.shortcuts import render
from django.http import HttpResponse

# TODO 1230学习  ↓
#  -----------------------------------------------------知识点1.
# TODO 面向过程 -- 函数 定义视图函数
def test(request):
# 使用postman发送post,get请求都可以,如何在视图函数中区分用户发送的请求类型? -- request.method
# 京东登录页面 点击刷新get请求 点击登录post请求 这时同一个页面需要区分get\post请求
    print(request.method)
    # 这时,用postman发送get\post请求时,控制台能显示GET\POST
    # TODO 根据不同请求方式去实现不同的业务逻辑 ↓
    if request.method == 'GET':
        return HttpResponse('您所使用的是get请求')
    else:
        return HttpResponse('您所使用的是post请求')
    # return HttpResponse('这是面向过程视图函数')

# 如京东登录页面 同一页面实现不同功能 用面向过程各种if else比较麻烦
# 采用面向对象方式 -- 类  类中除了属性 就是方法 定义一个类名,继承自xx,里面的方法 def get()  def post()
# TODO 面向对象 -- 不同业务逻辑放在方法里  -- 类视图  -- 可读性好、复用性高
#   1.类视图继承自View
#   2.类视图的方法是根据请求方式来实现的,用postman发送了一个get请求,实现类视图中的get方法,post就post
from django.views import View
class JDlogin(View):
    def get(self,request): #　self为类对应的实例对象,request为请求对象
        return HttpResponse('京东登录--get')
    def post(self,request):
        # self.abc() 但可以通过get post这两个函数实现
        return HttpResponse('京东登录--post')
    # 下一步去urls.py
    # path('jd/',JDlogin.as_view())
    def abc(self,request):
        return HttpResponse('abc') # 通过postman访问不到,因为View类中http_method_names里没有'abc'


# 面向对象回顾
"""
实例方法
class Person():
    def say(self):
        pass 
    p = Person() 调用
    p.say()
    
    @classmethod
    def eat(cls): # 类方法cls指的就是类本身 调用时不需要实例对象
        pass
    Person.eat() 调用
    
    @staticmethod
    def run(): # 静态方法第一个参数没要求
        pass
    Person.run() 调用

urls中,JDlogin.as_view() 就是通过类名去调用类方法, 类名.类方法, 继承的是父类View的类方法:as_view
 函数as_view嵌套view --装饰器 return view 调用as_view() 最后调用的是内层的view函数
    cls = JDlogin  cls()=JDlogin()   self=JDlogin()  return dispatch  dispatch是路由分发
"""

# TODO -----------------------------------------------知识点2.
#  京东未登录时点击查看我的订单,跳入注册页面
#  需求--访问个人中心页面,必须要求用户登录(后面讲解如何判断用户是否登录,先模拟假的)
# 1.定义个人中心类视图
# 2.必须要求用户登录
class CenterView(View):
    def get(self,request):
        islogin = True
        if islogin:
            # get展示个人信息
            return HttpResponse('center get')
        else:
            return HttpResponse('请登录')
    def post(self,request):
        islogin = True
        if islogin:
            # post修改个人信息
            return HttpResponse('center post')
        else:
            return HttpResponse('请登录')
# 如此写是否可以优化?
# TODO 每个函数都要写if else方法 麻烦 用装饰器可以,还可以使用 --- 多继承
#  系统有一个类(LoginRequiredMixin)可以帮助我们判断是否登录了 ,这个类重写dispatch方法 做了判断
from django.contrib.auth.mixins import LoginRequiredMixin
    # LoginRequiredMixin继承自AccessMixin,AccessMixin继承自object
    # 我们的CenterView要求要继承View和LoginRequiredMixin
    # class CenterView2(View,LoginRequiredMixin): 多继承第一种写法
    # class CenterView2(LoginRequiredMixin,View): 多继承第二种写法
    # 区别: 这两个父类都有dispatch 遵循mro查找顺序,验证: print(CenterView.__mro__)
    # 我们的期望是先验证是否登录,所以先继承LoginRequiredMixin,根据mro查找顺序,选择第二种
    # 自动导包:输入LoginRequiredMixin后光标在此时按alt+enter

class CenterView2(LoginRequiredMixin,View):
    # LoginRequiredMixin如果检测到没有登录的话,404报错,会跳转到/accounts/login页面
    def get(self,request):

        # get展示个人信息
        return HttpResponse('center get')

    def post(self,request):

        # post修改个人信息
        return HttpResponse('center post')
# TODO ------------------------------------------知识点3.中间件(前端 相对了解)
#  如何判断鱼是否上钩? --- 鱼要食物,鱼漂动能看到 -- 在请求和响应中间插入一些东西  中间件
#  ---使用中间件，在Django处理视图的不同阶段对输入或输出进行干预。  ---处理请求和响应时伴随发生的
"""
1.2 处理请求前的方法：(重要)
    在处理每个请求前，自动调用，返回None或HttpResponse对象
    def process_request(self, request):
         pass
1.5 处理响应后的方法：（重要）
    在每个响应返回给客户端之前，自动调用，返回HttpResponse对象
    def process_response(self, request, response):
         pass
"""
# TODO 详见 middleware文件中
# TODO 多个中间件执行顺序
#  在请求视图被处理前，中间件由上至下依次执行(请求按照注册顺序执行)
#  在请求视图被处理后，中间件由下至上依次执行(响应与请求反之)


# TODO ------------------------------------------知识点4.前端--Vue
"""
第一个Vue应用
1.导入vue.js
2.定义div标签盛放HTML
3.创建vue实例
"""
# sublime