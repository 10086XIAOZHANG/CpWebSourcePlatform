# CpWebSourcePlatform

#### 项目介绍

cp聚合博客--python后台

#### 软件架构

该平台采用Django2.0 xadmin  restframework api 开发


#### 使用说明

1. Django的版本要求必须是2.0版本,使之能和xadmin 对得上
2. GitHub 上面的xadmin 对Django的版本的选择还是存在诸多问题

#### 云之讯 其中注册会采用云之讯的短信服务

```
YUNZHIXUN_TOKEN = "****"
YUNZHIXUN_TEMPLATE_ID = "***"
```

#### 在utils/yunzhixun.py中提供func对云之讯的调用

#### mysql 配置账号密码

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "CpWebSourcePlatform",
        'USER': 'root',
        'PASSWORD': "*******",
        'HOST': "*****",
        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB;'}
    }
}
```

#### 在urls.py 中 主要配置api 匹配规则

```
urlpatterns = [
    # authentication / association
    url(r'^login/(?P<backend>[^/]+){0}$'.format(extra), views.auth,
        name='begin'),
    url(r'^complete/(?P<backend>[^/]+){0}$'.format(extra), views.complete,
        name='complete'),
    # disconnection
    url(r'^disconnect/(?P<backend>[^/]+){0}$'.format(extra), views.disconnect,
        name='disconnect'),
    url(r'^disconnect/(?P<backend>[^/]+)/(?P<association_id>\d+){0}$'
        .format(extra), views.disconnect, name='disconnect_individual'),
]
```

#### 通过social_django为项目提供第三方的分享


 ##博客地址：[link](https://www.cnblogs.com/fuGuy/)