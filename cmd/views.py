#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#import os
import json
from flask import render_template,request,redirect,session,flash
from cmd import cmd 
from models import User
from utils.web import login_required

#用户列表显示
@cmd.route('/')
@login_required
def cmd():
  return render_template('cmd.html')

