from flask import Flask

# from day01 import demo

# 1.0 创建flask的应用对象  核心     __name__魔法变量：当前文件所在模块的名字
app = Flask(__name__)

# 配置参数的使用方式
# 1.1使用配置文件
# app.config.from_pyfile("config.cfg")

# 1.3 直接操作config  字典
app.config["DEBUG"] = True


# 视图函数  用装饰器绑定路由
@app.route("/index")
def index():
    print("nihao")
    print(app.config.get("DEBUG"))
    return "你好啊  flask"


if __name__ == '__main__':
    app.run()
