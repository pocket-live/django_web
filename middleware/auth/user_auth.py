# -*- coding: utf-8 -*- 
# @Time : 2020/3/30 15:41 
# @Author : Pocket 
# @Desc : 用户登录鉴权中间件
from user_manage.models import SysUser
from user_manage import logger


class UserAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # logger.info(request.__dict__)
        print(request.POST)
        '''
        path、method、
        '''
        if request.path.startswith('/login'): # 登录
            pass

        # 执行路由前进行检测
        auth_error = self._auth_start(request)
        if auth_error:
            return
        response = self.get_response(request)

        return response

    def _auth_start(self, request):
        pass

    # 码云
