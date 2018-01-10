#-*- coding: utf-8 -*- 
#蓝本中定义的程序路由

from datetime import datetime
from flask import render_template, session, redirect, url_for

from .myblueprint import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		db.create_all()
		#检测是否存在
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			session['known'] = False
			user = User(username=form.name.data)
			db.session.add(user)

			#发送邮件
		else:
			session['known'] = True
			session['name'] = form.name.data
			form.name.data = ''

		return redirect(url_for('main.index'))  #注意url_for参数为点+index，等价于main.index
	return render_template('index.html',
							form=form, name=session.get('name'),
							known=session.get('known', False),
							currtent_time=datetime.utcnow())