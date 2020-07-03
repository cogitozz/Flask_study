from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from model import *
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:090200@localhost:3306/test1'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
# 上面的内容如果写在model.py中，会一直警告：UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:
# 导致在登录时总是报错sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: user
# db.init_app(app)    # 如果没有这一步，会报错 KeyError: 'SQLALCHEMY_TRACK_MODIFICATIONS'，参考https://www.cnblogs.com/String-Lee/p/10061675.html

from wtforms import Form,TextField,PasswordField,validators

class LoginForm(Form):
	username = TextField("username",[validators.Required()])
	password = PasswordField("password",[validators.Required()])


@app.route("/register",methods=['GET','POST'])
def register():
	myForm=LoginForm(request.form)
	if request.method=='POST':
		u=User(myForm.username.data,myForm.password.data)
		u.add()
		return redirect("http://www.jikexueyuan.com")
	return render_template('index.html',form=myForm)

@app.route("/login",methods=['GET','POST'])
def login():
	myForm=LoginForm(request.form)
	if request.method =='POST':
		u=User(myForm.username.data,myForm.password.data)
		if (u.isExisted()):
			return redirect("http://www.jikexueyuan.com")
		else:
			return "Login Failed"
	return render_template('index.html',form=myForm)

if __name__=="__main__":
	app.run(port=8080,debug=True)