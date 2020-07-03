from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')     # 这个代表着路由，输入 http://127.0.0.1:5000/就会调用该函数。
def hello_world():
    return 'Hello World!'

@app.route('/user', methods=['POST'])   # post请求，输入27.0.0.1:5000/user就会调用该函数
def hello_user():
    return 'hello user'

@app.route('/users/<id>')    # 可以输入127.0.0.1:5000/users/123，那么函数会读取123参数
def user_id(id):
    return 'hello user:'+id

@app.route('/query_user')
def query_user():
    id = request.args.get('id')     # 和上面的结果是一样的，需要输入127.0.0.1:5000/query_user?id=123
    return 'query user:'+id

@app.route('/query_url')
def query_url():
    return 'query url:'+url_for('query_user')   # 反向路由，通过视图反向导出url

if __name__ == '__main__':
    app.run()
