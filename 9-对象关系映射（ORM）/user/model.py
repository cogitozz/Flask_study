# model.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main_使用flask_sqlalchemy import *

app = Flask(__name__)
db.init_app(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:090200@localhost:3306/test1'
# # app.config['SQLALCHEMY_BINDS'] = 'mysql+pymysql://root:090200@localhost:3306/test1'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)
# db.create_all()	# 加上这一句使用pycharm启动没问题，但是在终端启动会报错ModuleNotFoundError: No module named 'MySQLdb'


class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(32),unique=True)
	password = db.Column(db.String(32))
	def __init__(self,username,password):
		self.username = username
		self.password = password
	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
			return self.id
		# except Exception,e:
		except :
			db.session.rollback()
			# return e
		finally:
			return 0
	def isExisted(self):
		temUser=User.query.filter_by(username=self.username,password=self.password).first()
		if temUser is None:
			return 0
		else:
			return 1


