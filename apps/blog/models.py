from datetime import datetime
from django.db import models
from  DjangoUeditor.models import UEditorField


# Create your models here.


class BlogActicle(models.Model):
    '''
      博客文章
    '''
    acticle_sn = models.CharField(max_length=50, default="", verbose_name="文章唯一标识", help_text="文章唯一标识")
    acticle_name = models.CharField(max_length=100, verbose_name="文章标题",help_text="文章标题")
    acticle_content = UEditorField(verbose_name=u"内容", imagePath="blog/images/", width=1000, height=300,
                                   filePath="blog/files/", default='',help_text="内容")
    comment_num = models.IntegerField(default=0, verbose_name="评价数",help_text="评价数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数",help_text="收藏数")
    click_num = models.IntegerField(default=0, verbose_name="点击数",help_text="点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.acticle_name


class BlogActicleBanner(models.Model):
    """
    轮播的文章图片
    """
    article = models.ForeignKey(BlogActicle, verbose_name="博客文章", on_delete=models.CASCADE,help_text="博客文章")
    image = models.ImageField(upload_to='blog/images/', verbose_name="轮播图片",help_text="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序",help_text="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article.acticle_name


class HotSearchWords(models.Model):
    """
    热搜词
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords


class BlogCategory(models.Model):
    '''
    博客文章类别
    '''
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
    )
    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "博客文章类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
