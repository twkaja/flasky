#-*- coding: utf-8 -*-
#导入蓝本
#通过将竞争资源main分离出来，使得导入views,errors
#不存在循环导入
from .myblueprint import main
from . import views, errors