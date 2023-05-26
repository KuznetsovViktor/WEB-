from flask import Flask
from flask import request
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!<p>"
@app.route("/test")
def test():
    return "<p>Viktor<p>"
@app.route("/test/test2")
def test2():
    return "<p>rydom<p>"
@app.route("/name/<user>")
def name(user):
    return "<p>Привет, {} <p>".format(user)
@app.route("/calc/sum/<a>/<b>")
def calc_sum(a,b):
    a = int(a)
    b = int(b)
    c = a+b
    return "<p>Сумма: {} <p>".format(c)
@app.route("/calc/del/<e>/<s>")
def calc_del(e,s):
    e = int(e)
    s = int(s)
    x = e/s
    return "<p>Деление: {} <p>".format(x)
@app.route("/calc/umn/<k>/<d>")
def calc_umn(k,d):
    k = int(k)
    d = int(d)
    f = k*d
    return "<p>Умножение: {} <p>".format(f)
@app.route("/calc/minus/")
def calc_minus():
    args_dict = request.args
    print(args_dict)
    a = float (args_dict["a"])
    b = float (args_dict["b"])
    c = a - b
    return "<p>Разность: {} <p>".format(c)
@app.route("/food")
def food():
    args_dict = request.args
    print(args_dict)
    a = args_dict["первое"]
    b = args_dict["второе"]
    c = 0
    d = 0
    if a == "суп":
        c = 100
    if a == "щи":
        с = 50
    if a == "борщ":
        с = 75
    if b =="макарошки":
        d = 60
    t = c+d
    return "<p>Стоимость за {} и {}: {} <p>".format(a,b,t)
@app.route("/mywaifu/<name>")
def mywaifu_pic(name):
    return '<img src="http://localhost:5000/static/{}.png" width="800" height="600">'.format(name)  
