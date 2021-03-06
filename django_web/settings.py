"""
Django settings for django_web project.

Generated by 'django-admin startproject' using Django 1.11.29.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8=l0vab5i^5au6-lo36xbk$)(i2wd1dr1j24d3cybrl#g-a3he'

# SECURITY WARNING: don't run with debug turned on in production!
'''
开启DEBUG模式:浏览器中和控制台会打印出错信息,这部分信息包含一些源码
关闭DEBUG模式：因为开启后会程序出错了会返回信息暴露一些源码，一般生产环境中会关闭
'''
DEBUG = False

'''
设置允许访问的ip地址服务
'''
ALLOWED_HOSTS = ['192.168.0.12','127.0.0.1','localhost','129.211.25.203']

# Application definition

'''
默认激活了一些应用，但并不是每个人都需要它们。如果你不需要某个或某些应用，
你可以在运行 migrate 前毫无顾虑地从 INSTALLED_APPS 里注释或者删除掉它们。 
migrate 命令只会为在 INSTALLED_APPS 里声明了的应用进行数据库迁移。
'''
INSTALLED_APPS = [
    'user_manage', # 也可以user_manage.apps.UserManageConfig
    # 'django.contrib.admin',  # 管理员站点
    'django.contrib.auth',  # 认证授权系统
    'django.contrib.contenttypes',  # 内容类型框架
    # 'django.contrib.sessions',  # 会话框架
    # 'django.contrib.messages',  # 消息框架
    # 'django.contrib.staticfiles',  # 管理静态文件的框架
    # 'rest_framework',  # rest ful 框架

]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # 安全中间件
    'django.contrib.sessions.middleware.SessionMiddleware', # 会话中间件
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # CSRF保护中间件
    'django.contrib.auth.middleware.AuthenticationMiddleware', # 验证中间件
    'django.contrib.messages.middleware.MessageMiddleware', # 消息中间件
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # X-Frame-Options中间件
    'middleware.auth.user_auth.UserAuthMiddleware' # 自定义登录认证中间件
]

ROOT_URLCONF = 'django_web.urls'

# 模版
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_web.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

'''
数据库配置：
ENGINE的可选值有：
    1.django.db.backends.sqlite3
    2.django.db.backends.postgresql
    3.django.db.backends.mysql
    4.django.db.backends.oracle
    
除了官方支持的数据库外，还有第三方提供的后端。（比如：IBM DB2）
'''
DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3', # sqlite3版本需要大于3.8 可以利用sqlite3 --version检测版本号
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), # 如果使用的是 SQLite， NAME 应该是此文件的绝对路径。默认值 os.path.join(BASE_DIR, 'db.sqlite3') 将会把数据库文件储存在项目的根目录
        # 'ENGINE': 'django.db.backends.mysql',  # 引擎
        # 'NAME': 'db_dj', # 数据库名称
        # 'USER': 'root', # 用户名
        # 'PASSWORD': '123456', # 密码
        # 'HOST': '127.0.0.1' # ip地址
    # }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 设置静态文件的URL路径记忆文件夹位置
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

# 缓存设置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
