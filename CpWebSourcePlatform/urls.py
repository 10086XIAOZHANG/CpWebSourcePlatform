"""CpWebSourcePlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls import include, url
from django.urls import include, path
import xadmin
from CpWebSourcePlatform.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from blog.views import BlogActicleBannerListViewSet, BlogActicleListViewSet, BlogCategoryListViewSet
from users.views import UserViewset,SmsCodeViewSet
from user_operation.views import UserFavViewSet,UserLeavingMessageViewSet,UserCommentViewSet
router = DefaultRouter()
router.register(r'users', UserViewset, base_name='user')
router.register(r'code', SmsCodeViewSet, base_name='code')
router.register(r'blogActicle', BlogActicleListViewSet, base_name='blogActicle')
router.register(r'blogActicleBanner', BlogActicleBannerListViewSet, base_name='blogActicleBanner')
router.register(r'blogCategory', BlogCategoryListViewSet, base_name='blogCategory')
router.register(r'userFavs', UserFavViewSet, base_name='userFavs')
router.register(r'userLeavingMessage', UserLeavingMessageViewSet, base_name='userLeavingMessage')
router.register(r'userComment', UserCommentViewSet, base_name='userComment')
blogActicle_banner_list = BlogActicleBannerListViewSet.as_view({
    'get': 'list',  # get 绑定到list
})

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),
    url('docs/', include_docs_urls(title="CP 聚合博客")),
    url(r'^login/$', obtain_jwt_token),
    # 第三方登陆
    url('', include('social_django.urls', namespace='social')),
]
