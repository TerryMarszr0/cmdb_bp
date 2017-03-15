#!/user/bin/env python
#encoding: utf-8
from flask import session, redirect
from functools import wraps
def login_required(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    if session.get('user') is None:
      return redirect('/login')
    rt = func(*args, **kwargs)
    return rt
  return wrapper
