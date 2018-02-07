from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)


class Tag(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)


class Post(models.Model):
    def __str__(self):
        return self.title
    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文
    body = models.TextField()

    # 文章创建时间和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要,可以为空
    excerpt = models.CharField(max_length=200, blank=True)

    # 每篇文章只有一个分类, 每个分类对应多个文章, 分类和文章是一对多的关系
    # 每篇文章有多个标签, 每个标签有多篇文章, 标签和文章是多对多的关系, 文章可以没有标签
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者, 使用django内置的模型
    author = models.ForeignKey(User)
