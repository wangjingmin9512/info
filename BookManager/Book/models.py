from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    # TODO 修改admin网站添加成功后的书籍名字为添加的名字 而不是BookInfo object (1)
    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    Book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    # TODO 修改admin网站添加成功后的人物名字为添加的名字 而不是BookInfo object (1)
    def __str__(self):
        return self.name