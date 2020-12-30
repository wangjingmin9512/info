# TODO 3.中间件  -- 处理请求和响应伴随发生的
# 1.导包 MiddlewareMixin
from django.utils.deprecation import MiddlewareMixin
# 2.定义中间件类
class BookMiddlewareMixin(MiddlewareMixin):
    def process_request(self,request):
        print('request处理请求前被调用1')
    def process_response(self,request,response):
        print('response响应返回给客户端前被调用1')
        return response

class BookMiddlewareMixin2(MiddlewareMixin):
    def process_request(self,request):
        print('request处理请求前被调用2')

    def process_response(self,request,response):
        print('response响应返回给客户端前被调用2')
        return response
# 3. 注册安装自定义中间类
# settings → 与安装子应用类似
#  'book,middleware.BookMiddlewareMixin',
#  'book,middleware.BookMiddlewareMixin2',

# 4. 验证多个不同中间件执行顺序  -- 使用postman POST方式请求index页面
# request处理请求前被调用1   请求中间件按照settings中的注册顺序由上至下执行，响应中间件反之
# request处理请求前被调用2
# POST
# response响应返回给客户端前被调用2
# response响应返回给客户端前被调用1
