from django.db import models
# TODO 1226第二步 导django红线报错,设置安装了django的解释器 -- py3_wjm_1224
# Create your models here.
# TODO 1226第三步 创建模型类BookInfo 和 PeopleInfo
class BookInfo(models.Model):
    name = models.CharField(max_length=10, verbose_name='书籍名称')
    pub_date = models.DateField(verbose_name='发布日期',null=True)  # 允许为空
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'bookinfo'  # 将默认表名book_bookinfo(小写app应用名_小写模型类名)指明为bookinfo
        verbose_name = '图书'

    def __str__(self):
        return self.name  # 每条数据的显示信息为书籍名称了

class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0,'male'),
        (1,'female')

    )
    name = models.CharField(max_length=20,verbose_name='人物名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0,verbose_name='性别')
    description = models.CharField(max_length=20, null=True,verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE,verbose_name='图书')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name

