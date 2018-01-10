#数据库模型
#db定义在当前的包内
from . import db 
#加入密码散列
from werkzeug.security import generate_password_hash, check_password_hash
#支持用户验证
from flask_login import UserMixin

#Role类
class Role(db.Model):
	__tablename__ = 'roles'
	#名字不允许重复
	name = db.Column(db.String(64), unique=True)
	#主键
	id = db.Column(db.Integer, primary_key=True)
	#关系
	#这里的role是单数，(一对多关系)一个角色对应多个用户
	users = db.relationship('User', backref='role') #lazy='dynamic')



#User类
class User(UserMixin, db.Model):
	__tablename__ = 'users'
	email = db.Column(db.String(64), unique=True, index=True)
	username = db.Column(db.String(64), unique=True, index=True)
	id = db.Column(db.Integer, primary_key=True)
	#roles.id作为外键
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	#类熟悉，实例不可访问
	password_hash = db.Column(db.String(128))

	#设置password属性
	@property
	def password(self):
		raise AttributeError('password is not readable')
	#可写
	@password.setter
	def password(self, mypassword):
		#password是User属性，由于上面设置了不可访问，所以只能能不访问
		#且不能使用self.password访问
		#print(password)
		#实例属性
		self.password_hash = generate_password_hash(mypassword)
	#检测密码正确性
	
	def verify_password(self, password):
		#print(self.password_hash)
		return check_password_hash(self.password_hash, password)


#flask_login要求实现的回调函数
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))