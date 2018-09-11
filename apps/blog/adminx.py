# -*- coding: utf-8 -*-
__author__ = 'bobby'

import xadmin
from .models import BlogActicle, BlogCategory, BlogActicleBanner, HotSearchWords


class BlogActicleBannerAdmin(object):
    list_display = ["article", "image", "index", ]
    model_icon = 'fa fa-barcode'


class BlogActicleAdmin(object):
    list_display = ["acticle_sn", "acticle_name", "acticle_content", "comment_num", "fav_num", "click_num",
                    "add_time"]
    model_icon = 'fa fa-book'


class HotSearchWordsAdmin(object):
    list_display = ["keywords", "index", "add_time", ]
    model_icon = 'fa fa-building-o'


class BlogCategoryAdmin(object):
    list_diplay = '__all__'
    model_icon = 'fa fa-bookmark-o'


xadmin.site.register(BlogActicle, BlogActicleAdmin)
xadmin.site.register(BlogCategory, BlogCategoryAdmin)
xadmin.site.register(BlogActicleBanner, BlogActicleBannerAdmin)
xadmin.site.register(HotSearchWords, HotSearchWordsAdmin)
