# -*- coding: UTF-8 -*-
import flask
import pymysql
app = flask.Flask(__name__, template_folder='templates')


# 创建mysql表
def createTable(cursor):
    # 创建message 数据库, 如果存在则删除message 数据库
    cursor.execute("drop database if exists message")
    cursor.execute("create database message")
    # 选择 message 这个数据库
    cursor.execute("use message")

    # 如果存在这个表则删除
    cursor.execute("drop table if exists message")
    # sql中的内容为创建一个名为message的表
    sql = """CREATE TABLE IF NOT EXISTS `message` (
              `nickname` VARCHAR (100),
              `text` VARCHAR (1000)
              )"""
    # 创建表
    cursor.execute(sql)

    print("successfully create table")


@app.route('/', methods=['GET', 'POST'])
def index():
    return flask.render_template("index.html")


@app.route('/index', methods=['GET', 'POST'])
def index0():
    return flask.render_template("index.html")


@app.route('/index-01', methods=['GET', 'POST'])
def index1():
    return flask.render_template("index-01.html")


@app.route('/index-02-01', methods=['GET', 'POST'])
def index21():
    return flask.render_template("index-02-01.html")


@app.route('/index-02-02', methods=['GET', 'POST'])
def index22():
    return flask.render_template("index-02-02.html")


@app.route('/index-02-03', methods=['GET', 'POST'])
def index23():
    return flask.render_template("index-02-03.html")


@app.route('/index-03-01', methods=['GET', 'POST'])
def index31():
    return flask.render_template("index-03-01.html")


@app.route('/index-03-02', methods=['GET', 'POST'])
def index32():
    return flask.render_template("index-03-02.html")


@app.route('/index-03-03', methods=['GET', 'POST'])
def index33():
    return flask.render_template("index-03-03.html")


@app.route('/index-04', methods=['GET', 'POST'])
def index4():
    if flask.request.method == 'POST':
        tmp = flask.request.get_data()
        tmp = tmp.decode("ascii")
        tmp = tmp.split("&")
        print(tmp)
        ans = []
        for i in tmp:
            i = i.split("=")
            ans.append(i[1])
        sql = """insert into message(nickname, text) values (\'%s\', \'%s\')""" % (ans[0], ans[1])
        print(sql)
        cursor.execute(sql)
        db.commit()
    # 选择全部
    cursor.execute("select * from message")
    # 获得返回值，返回多条记录，若没有结果则返回()
    results = cursor.fetchall()

    # 前端需要的data
    data = []

    # 遍历打印
    for row in results:
        name = row[0]
        text = row[1]
        data.append([name, text])
        print("name =", name, " text =", text, '\n')

    return flask.render_template("index-04.html", data=data)


if __name__ == '__main__':
    # 连接数据库
    db = pymysql.connect("localhost", "root", "", charset="utf8")
    # 创建数据库指针
    cursor = db.cursor()
    createTable(cursor)
    app.run()
