
from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=150, null=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'admin'


class Category(models.Model):
    c_name = models.CharField(max_length=10, unique=True)
    f = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    alias = models.CharField(max_length=10, null=True)
    keywords = models.CharField(max_length=20, default='无')
    desc = models.TextField(max_length=200, default='无')
    nums = models.IntegerField(default=0)

    class Meta:
        db_table = 'category'


class Acticle(models.Model):
    title = models.CharField(max_length=20, unique=True)
    contents = models.TextField(default='无', null=False)
    desc = models.CharField(max_length=300, null=True)
    keyword = models.CharField(max_length=20, null=True)
    tags = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='upload', null=True)
    visibility = models.BooleanField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    c = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'acticle'



