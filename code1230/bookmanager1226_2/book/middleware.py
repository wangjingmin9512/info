from django.utils.deprecation import MiddlewareMixin
# TODO 1.定义1个中间件
class BookMiddlewareMixin(MiddlewareMixin):
    # 每次请求前都会调用
    def process_request(self,request):
        print('request每次处理请求前都会调用 1')

    # 每次响应前都会调用
    def process_response(self,request,response):
        print('response每次响应返回给客户端前都会调用 1')
        # 响应要返回
        return response
# TODO 定义完  还要告诉系统  settings 注册
#  注册完后,访问视图函数 如test 使用get请求访问
#  控制台打印结果如下:
# request每次请求前都会调用
# GET
# response每次响应前都会调用
# TODO 1.定义2个中间件
class BookMiddlewareMixin2(MiddlewareMixin):
    # 每次请求前都会调用
    def process_request(self,request):
        print('request每次处理请求前都会调用 2')

    # 每次响应前都会调用
    def process_response(self,request,response):
        print('response每次响应返回给客户端前都会调用 2')
        # 响应要返回
        return response
# TODO 多个中间件执行顺序
#  在请求视图被处理前，中间件由上至下依次执行(请求按照注册顺序执行)
#  在请求视图被处理后，中间件由下至上依次执行(响应与请求反之)
# request每次请求前都会调用 1      请求按照注册顺序执行
# request每次请求前都会调用 2
# GET
# response每次响应前都会调用 2     响应反着注册顺序执行
# response每次响应前都会调用 1
