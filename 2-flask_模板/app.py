from flask import Flask, render_template
from models import User

app = Flask(__name__)


@app.route('/')
def hello_world():
    content = "Hello world"
    return render_template("index.html", content=content)   # 返回模板的内容，同时将content传给模板实现前后端交互

@app.route('/user')
def user_index():
    user = User(1, 'jikexueyuan')   # 使用models是为了将更复杂的信息传给前端
    return  render_template("user_index.html", user=user)

@app.route('/query_user/<user_id>')
def query_user(user_id):
    user = None
    if int(user_id) == 1:       # 在模板中实现了if语句
        user = User(1, 'jikexueyuan')
    return render_template("user_id.html",user=user)

@app.route('/users')
def user_list():
    users = []
    for i in range(1,11):       # 在模板中实现了for语句
        user = User(i, 'jikexueyuan'+str(i))
        users.append(user)
    return render_template("user_list.html",users=users)

@app.route('/one')
def one_base():
    return  render_template("one_base.html")    # 在模板中实现了模板的继承

@app.route('/two')
def two_base():
    return  render_template("two_base.html")

if __name__ == '__main__':
    app.run()
