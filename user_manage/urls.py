# -*- coding: utf-8 -*- 
# @Time : 2020/3/23 23:01 
# @Author : Pocket 
# @Desc :
from django.urls import path

from . import user_api

# 配置url每个路径映射的方法
urlpatterns = [
    path('insertUser', user_api.insert_data, name='insertUser'),
    path('deleteUser', user_api.delete_data, name='deleteUser'),
    path('getUser', user_api.search_data, name='getUser'),
]