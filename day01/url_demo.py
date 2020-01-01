from flask import Flask, current_app, redirect, url_for, request, abort, Response
import json

# from day01 import demo

# 1.0 创建flask的应用对象  核心     __name__魔法变量：当前文件所在模块的名字
app = Flask(__name__)

# 配置参数的使用方式
# 1.1使用配置文件
# app.config.from_pyfile("config.cfg")

# 1.3 直接操作config  字典
app.config["DEBUG"] = True


# 视图函数  用装饰器绑定路由
@app.route("/index", methods=["post", "get"])
def index():
    # request中包含了前端  发送过来的请求数据   form 是一个类字典的对象
    name = request.form.get("name")
    age = request.form.get("age")
    data = request.data
    args = request.args

    return "你好啊  flask   name %s,age %s,data %s" % (name, age, data)


@app.route("/uploadFile", methods=["post"])
def upload_file():
    file_obj = request.files.get("file")
    if file_obj is None:
        return "没有上传文件"
    # with open("demo.config","wb") as file:
    #     file.write(file_obj.read())
    file_obj.save("redis")
    return "成功接收到了文件。"


@app.route("/postOnly", methods=["post"])
def postOnly():
    data = dict()
    

    json.dump()
    print(app.config.get("DEBUG"))
    return "你好啊  flask  设置http的请求方式。"


@app.route("/login")
def login():
    # url="/index"  # 写死的方式
    url = url_for("index")  # url_for  反解析
    return redirect(url)


@app.route("/goods/<int:good_id>")
def get_goods(good_id):
    return "接受到的参数%s" % good_id


@app.route("/test_abort")
def test_abort():
    name = request.args.get("name")
    age = request.args.get("age")
    if age != str(26) or name != "段振科":
        # abort 函数可以立刻终止视图函数的执行  传递给前端 信息 （1.0:  状态码  2.0 ：返回响应对象 ）
        resp = Response("登录失败了")
        abort(resp)
    return "成功测试abort 函数了！！！！"


@app.errorhandler(404)
def handle_error(err):
    """# 自定义错误处理试图函数"""
    return u"出现了404错误，错误信息%s" % err


if __name__ == '__main__':
    print(app.url_map)  # app.url_map  存放了所有的  路由映射规则
    app.run(debug=True)
