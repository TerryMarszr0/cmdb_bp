#!/usr/bin/env python
#encoding: utf-8
from flask import Flask
from login import log
from user import user

app = Flask(__name__, static_folder='static')
# 生成随机32位的KEY, os.urandom(32)
app.secret_key = '\x11\x1fL\x931M\x16I\x8f\xddR\xc2jk\xe37\xdf\xbd\x8f\xd1\x9c\x9e\x1c\x1c\x89o\xc8\xa7\xf2\xe7H^'

app.register_blueprint(log)
app.register_blueprint(user, url_prefix='/user')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9001, debug=True)
