#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#import os
import json
from flask import render_template,request,redirect,session,flash
from user import user
from models import User
from utils.web import login_required

#用户列表显示
@user.route('/')
@login_required
def users():
  user_list=User.get_list()
  return render_template('users.html', user_list=user_list)

#跳转到新建用户信息输入的页面
@user.route('/create/', methods=['POST','GET'])
@login_required
def createuser():
  return render_template('user_create.html') 

#提交新建用户的信息
@user.route('/add/', methods=['POST'])
@login_required
def add_user():
  username = request.form.get('username', '')
  password = request.form.get('password', '')
  age = request.form.get('age','')

  _user = User(username=username, password=password, age=age)
  _is_ok, _errors = _user.validate_add2()
  print _errors
  if _is_ok:
    _user.save()

  return json.dumps({'is_ok':_is_ok, "errors":_errors, 'success':'添加成功'})
'''
  #检查用户信息
  _is_ok, _error = User.validate_add(username, password, age)

#  if _is_ok:
#    user.add_user(username, password, age)  # 检查OK，添加用户信息
#    return redirect(url_for('users', msg='新建成功'))
#  else:
#    # 跳转到用户新建页面，回显错误信息&用户信息
#    return render_template('create_user.html', \
#                            error=_error, username=username, \
#                            password=password , age=age)
  if _is_ok:
    User.add(username, password, age)  # 检查OK，添加用户信息
'''

# 用户修改页面
@user.route('/modify/',methods=['POST','GET'])
@login_required
def modify_user():
  username = request.args.get('username', '')
  _user = User.get_by_name(username)
  return render_template('user_modify.html', user=_user)

# 提交用户修改数据
@user.route('/update/', methods=['POST'])
@login_required
def update_user():
  # 检查用户信息
  _is_ok, _errors = User.validate_update(request.form)

#  if _is_ok:
#    user.update_user(username, password, age)  # 检查OK，添加用户信息
#    flash('修改用户信息成功')
#    return redirect('/users/')
#  else:
#    # 跳转到用户新建页面，回显错误信息&用户信息
#    return render_template('modify_user.html', \
#                            error=_error, username=username, \
#                            password=password , age=age)
  if _is_ok:
    User.update(request.form)  # 检查OK，更新用户信息

  return json.dumps({'is_ok':_is_ok, "error":_errors, "success":"更新成功"})

@user.route('/delete/')
@login_required
def delete_user():
  username = request.args.get('username','')
  User.delete(username)
  flash('删除用户信息成功')
  return redirect('/user/')

# 用户修改页面
@user.route('/modify-password/',methods=['POST','GET'])
@login_required
def modify_password():
  username = request.args.get('username', '')
  _user = User.get_by_name(username)
  return render_template('user_modify-password.html', user=_user)

@user.route('/change-password/', methods=['POST'])
@login_required
def change_user_password():
  username=request.form.get('username')
  manager_password=request.form.get('mpassword')
  user_password=request.form.get('upassword')

  print username, manager_password, user_password,session['user']['username']
  _is_ok, _errors = User.validate_change_password(username, user_password , \
                    session['user']['username'], manager_password)
  if _is_ok:
    User.change_password(username,user_password)

  return json.dumps({'is_ok':_is_ok, "errors":_errors,"success":"更新密码成功"})

@user.route('/logout/')
@login_required
def logout():
  session.clear()
  print session
  return redirect('/login')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=9001,debug=True)
