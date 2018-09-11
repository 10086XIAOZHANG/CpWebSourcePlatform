from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q;
from random import choice
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from utils.yunzhixun import YunZhiXun
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from django.contrib.auth import get_user_model

User = get_user_model()
from CpWebSourcePlatform.settings import YUNZHIXUN_TEMPLATE_ID, YUNZHIXUN_TOKEN
from .serializers import UserRegSerializer, UserDetailSerializer, SmsSerializer
from .models import VerifyCode


# Create your views here.
class CustomBackend(ModelBackend):
    '''
        用户自定义认证
    '''

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewset(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户 新增/修改/获取
    """
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    # 动态设置serializer
    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer
        return UserDetailSerializer

    # 动态设置接口权限
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []
        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username
        re_dict["user_id"] = user.id

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    # get list or delect
    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


class SmsCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
      发送验证码
    '''
    serializer_class = SmsSerializer

    def generate_code(self):
        '''
            生成四位数验证码
        :return: 四位数验证码
        '''
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        '''
            重写create
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]

        yun_zhi_xun = YunZhiXun(YUNZHIXUN_TOKEN)

        code = self.generate_code()
        sms_status = yun_zhi_xun.send_sms(templateId=YUNZHIXUN_TEMPLATE_ID, mobile=mobile, code=code, timeout=2)

        if sms_status["code"] != '000000':
            return Response({
                "mobile": sms_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                "mobile": mobile
            }, status=status.HTTP_201_CREATED)
