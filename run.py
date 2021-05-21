from flask import Flask, redirect, url_for, request, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix
import multiprocessing, threading
import requests
from config import SECRET_KEY
import logging

logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='log_new.log',  # 将日志写入log_new.log文件中
                    filemode='a',#模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )

app = Flask(__name__, static_url_path='')
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db/cloud.db'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = SECRET_KEY
app.wsgi_app = ProxyFix(app.wsgi_app)
db = SQLAlchemy(app)

from manage import manage

app.register_blueprint(manage, url_prefix='/disk')

from admin import admin

app.register_blueprint(admin, url_prefix='/admin')


@app.route('/')
def hello_world():
    return redirect(url_for('manage.home'))


@app.route('/404/')
def get_error():
    return '404-抱歉您无法访问此网页'

from manage.dropFiles import drop_files

"""
这里开的一个进程目的是为了执行定时回收站文件清理
在/manage/dropFiles
实测这里是没用的，所以只能手动把这个脚本起来。。。
"""
if __name__ == '__main__':
    app.run(debug=False)
