#-*- coding: utf-8 -*- 
#启动脚本

import os 
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

#自定义单元测试命令
@manager.command 
def test():
	'''运行测试'''
	import unittest
	#自动寻找tests包中的测试文件
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
	manager.run()
