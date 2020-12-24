from Book.views import index222
from django.urls import path

urlpatterns=[
    # TODO path中第一个参数是用户访问路由，第二个参数是视图函数名
    path('index/', index222)

]