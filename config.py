#-*- coding: utf-8 -*-
#flask配置文件，采用类的形式

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#config基类
#python3基类无需继承Object
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess'  #密匙
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #程序销毁自动提交保存数据库
    FLASKY_MAIL_SUBJECT = ['Flasky']  #主题，这里是列表的形式
    FLASKY_MAIL_SENDER = 'Flask Admin <1075519408@qq.com>'  #邮件发送者
    FLASKY_ADMIN = os.getenv('FLASKY_ADMIN')  #系统管理员


    @staticmethod
    def init_app(app):
    	pass


#我觉得这应该叫EmailConfig
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')  #邮箱账号
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORS')  #授权码
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
        
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

                                                                        
    