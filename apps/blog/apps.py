from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = "博客管理"
    model_icon = "fa fa-bars"