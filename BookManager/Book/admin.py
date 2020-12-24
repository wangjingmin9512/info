from django.contrib import admin
from Book.models import BookInfo,PeopleInfo
# Register your models here.
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)