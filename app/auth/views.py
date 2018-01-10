#-*- coding: utf-8 -*- 
#auth蓝图视图函数
from . import auth
from flask import render_template, flash, url_for, request, redirect
from .forms import LoginForm
from ..models import User
from flask_login import login_user, logout_user, login_required
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	db.create_all()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		#用户存并且密码正确
		if user is not None and user.verify_password(form.password.data):
			#把用户标记为已登录
			login_user(user, form.remember_me.data)
			#从next参数查询跳转前的页面
			return redirect(request.args.get('next') or url_for('main.index'))
		flash('用户名或者密码错误')
	return render_template('auth/login.html', form=form)
#登出
@auth.route('/logout', methods=['GET','POST'])
@login_required
def logout():
	logout_user()	
	return redirect(url_for('auth.login'))