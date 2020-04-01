# -*- coding: utf-8 -*- 
# @Time : 2020/3/25 22:08 
# @Author : Pocket 
# @Desc :
import unittest
import requests
from functools import wraps

from tools.logRecorder import LogRecorder

logger = LogRecorder(level='DEBUG', is_show_line=False).logger

POCKET = 'pocket'
XYL = 'xyl'


def result_print_func(f):
    '''
    结果返回打印装饰器
    '''

    @wraps(f)
    def wrapper_function(*args, **kwargs):
        response = f(*args, **kwargs)
        try:
            logger.info('%s%s%s%s%s%s%s%s' % (
            response.request.method, ':', response.request.url, '\n', '状态:', response.status_code, '\t结果:',
            response.json()))
        except Exception as e:
            logger.error('%s' % (e))

    return wrapper_function


def api_url(url, name=POCKET):
    '''
    路由装饰器
    '''

    def func(f):
        @wraps(f)
        def wrapper_function(*args, **kwargs):
            try:
                ts = args[0]
                host = ts.pocket_host if name == POCKET else ts.xyl_host
                kwargs.update({'url': host + url})
                return f(*args, **kwargs)
            except Exception as e:
                logger.error('%s' % (e))

        return wrapper_function

    return func


class APITestCase(unittest.TestCase):
    '''
    测试api程序
    '''
    pocket_host = 'http://localhost:8099/'
    xyl_host = 'http://192.168.0.4:8000/'

    @classmethod
    def setUpClass(cls):
        logger.info('开始测试>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

    @api_url('user_manage/insertUser')
    @result_print_func
    def test_insertUser(self, url=''):
        res = requests.post(url, data={'name': '56776'})
        return res

    @api_url('customer/add_data', name=XYL)
    @result_print_func
    def test_add_data(self, url=''):
        print(url)
        res = requests.get(url, params={
            'user_id': 'pocket_test',
            'iphone': '18379215236',
            # 'email':'1178699765@qq.com',
            'password': '12345678'
        })
        return res


if __name__ == '__main__':
    unittest.main()
