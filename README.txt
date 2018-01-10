a.文件夹说明
我简化了结构，虚拟环境包venv和数据库迁移包migrations被我移除了
	1.app  -----  flask程序
	    -templates  存放模板文件
	    -static  存放静态文件(图片等资源)
	    -main  存放flask程序代码
		
	    -__init__.py  app是个包
	    -email.py  flask发送邮件
	    -models.py 数据库模型

	2.tests  -----  单元测试
	    -__init__.py 同上
	    -test.py. 单元测试文件

	3.requirements.txt  flask程序依赖的所有包
	4.config.py  flask程序的所有配置
	5.manage.py  用于启动程序以及其他任务