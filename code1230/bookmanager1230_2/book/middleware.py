from django.utils.deprecation import MiddlewareMixin
class BookMiddlewareMixin1(MiddlewareMixin):
    def process_request(self,request):
        print('request在每次处理请求前被调用1')
    def process_response(self,request,response):
        print('response在响应未返回客户端前被调用1')
        return response

class BookMiddlewareMixin2(MiddlewareMixin):
    def process_request(self,request):
        print('request在每次处理请求前被调用2')
    def process_response(self, request, response):
        print('response在响应未返回客户端前被调用2')
        return response

# 多个中间件执行顺序： 按照注册的上下顺序， 请求自上而下，响应自下而上
# 访问路由为check1/，控制台打印结果
# request在每次处理请求前被调用1
# request在每次处理请求前被调用2
# GET
# response在响应未返回客户端前被调用2
# response在响应未返回客户端前被调用1
