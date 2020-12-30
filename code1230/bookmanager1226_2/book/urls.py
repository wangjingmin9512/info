from book.views import test
from django.urls import path
from book.views import JDlogin,CenterView,CenterView2



urlpatterns = [
    path('test/', test), # 视图函数第一个参数是url,第二个参数为视图函数的名字
    # TODO 1.类视图配置path第一个参数是url,第二个参数直接写JDlogin肯定不行,因为是类名不是函数名
    path('jd/',JDlogin.as_view()),
    path('center/',CenterView.as_view()),  # TODO 2.个人中心path
    path('center2/',CenterView2.as_view()),  # TODO 2.个人中心path

]
