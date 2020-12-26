# TODO 1226第七步.URLconf配置-子应用中
from django.urls import path
from book.views import index,book,book2,login,weibo

urlpatterns = [
    path('index/',index),  # 第二个参数为views.py中的函数名,不一定非要和url相同
    path('<cat_id>/<detail_id>/', book), # TODO Type1.GET请求 url 对应book模型函数
    path('<cat_id>/<detail_id>/', book2), #　TODO Type2.GET请求 查询字符串 对应book2模型函数,测试此种需注释掉Type1
    # TODO 如果GET请求URL和查询字符串两种都想保留且正常运行,则可以设置两个路径的层级不同,如URL的是1/100 查询字符串的是1/100/200/?a=10&b=20
    path('login/',login),  # TODO Type3. POST请求 表单类型 对应login函数
    path('weibo/',weibo),
]
# TODO 1226第八步 执行迁移
# pycharm终端中 python manage.py makemigrations
#              python manage.py migrate
# TODO 1226第九步 访问127.0.0.1:8000/index/网址测试是否运行成功
#                桌面终端选择bookmanager1226查看是否生成两个数据表--bookinfo和peopleinfo
# TODO 1226第十步 桌面终端在两个数据表中分别插入指定数据 insert into...
# TODO 第十一步见book.views.py
