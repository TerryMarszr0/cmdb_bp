#encoding:utf-8
from utils.dbutils import MySQLConnection
import time
#from dbutils import execute_fetch_sql , execute_commit_sql

class User(object):
  def __init__(self, username, password, age):
    self.username = username
    self.password = password
    self.age = age

  # 验证用户名，密码是否正确
  @classmethod
  def validate_login(cls, username, password):
    _column='username'
    _columns = _column.split(',')
    _sql = "select {column} from user where username=%s and password=md5(%s)".format(column=_column)
    _count, _rt_list = MySQLConnection.execute_sql(_sql, (username, password))
    return dict(zip(_columns , _rt_list[0])) if _count != 0 else None

