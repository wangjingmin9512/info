from django.urls import path
from book.views import if_else_checkpage,Check_request,Check_orders
urlpatterns = [
    path('check1/',if_else_checkpage),  # TODO 1.面向过程 实现判断用户请求方式get\post返回不同页面
    path('check2/',Check_request.as_view()),  # TODO 2.类视图 实现如上功能
    path('check3/',Check_orders.as_view()),  # TODO 3.类视图多继承 LoginRequiredMixin
]