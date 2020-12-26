from book.views import index,book,book2,login,weibo
from django.urls import path

urlpatterns = [
    path('index/',index),
    path('<cat_id>/<detail_id>/<c_id>/', book),
    path('<cat_id>/<detail_id>/', book2),
    path('login/',login),
    path('weibo/', weibo)
]