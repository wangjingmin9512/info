from django.urls import path
from book.views import test,index,JDlogin,Ifelse_checkorders,Check_orders
urlpatterns = [
    path('test/',test),  # 测试是否正常运行
    path('index/',index),  # 面向过程方式判断请求为get\post
    path('Center/',JDlogin.as_view()),  # 面向对象方式判断请求为get\post
    path('center/',Ifelse_checkorders.as_view()), # 单继承实现未登录时查看订单跳转登录界面
    path('check/',Check_orders.as_view()), # 多继承未登录跳转url为 accounts/login/?next=/check/
]