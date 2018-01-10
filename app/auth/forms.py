#-*- coding: utf-8 -*- 
#登录表单
from flask_wtf import FlaskForm 
#BooleanField复选框
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email(), Length(1,64)])

	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('keep me logged in')
	submit = SubmitField('Log In')