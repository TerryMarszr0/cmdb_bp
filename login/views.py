#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#import os
import json
from flask import render_template,request,redirect,session,flash
from login import log
from models import User

@log.route('/')
def index():
  return render_template('login.html')

@log.route('/login/',methods=['POST','GET'])
def login():
  params = request.args if request.method == 'GET' else request.form
  username = params.get('username','')
  password = params.get('password','')

  _user = User.validate_login(username, password)
  if _user :
    session['user'] = _user
    print _user
    return redirect('/user/')
  else:
    return render_template('login.html',username=username, error='username or password is error.')

