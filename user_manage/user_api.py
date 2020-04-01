'''
用户api
这里我们不进行视图创作，直接以restful api风格返回数据
'''
from django.http import HttpResponse

from functools import wraps

from django.views.decorators.csrf import csrf_exempt

from user_manage.models import SysUser
from . import logger


def login():
    '''
    登录
    :return:
    '''
    pass


def logout():
    '''
    退出登录
    :return:
    '''
    pass


def token_auth(func):
    '''
    token验证
    :param func:
    :return:
    '''

    @wraps(func)
    def wrapper_function(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper_function


import json

'''
@csrf_exempt:CSRF验证,django的跨站请求拦截，这里我们关闭这个功能，让post可以请求进来
也可以在setting.py里注释django.middleware.csrf.CsrfViewMiddleware
'''


@csrf_exempt
@token_auth
def insert_data(request):
    '''
    插入用户信息
    :return:
    '''
    print(3)
    if request.method == 'POST':
        result = {'code': 200, 'msg': '成功', 'data': {'name': 'pocket', 'age': 25}}
        return HttpResponse(json.dumps(result), content_type='application/json')


@token_auth
def delete_data(request):
    '''
    删除用户信息
    :return:
    '''
    print(request.__dict__.items())
    return HttpResponse('%s' % request.__dict__.items())


@token_auth
def search_data(request):
    '''查询用户信息'''
    pass
