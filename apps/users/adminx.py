import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "CP聚合博客后台"
    site_footer = "CP聚合博客"
    menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_diplay = '__all__'
    model_icon = 'fa fa-building-o'

xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(views.CommAdminView, GlobalSetting)