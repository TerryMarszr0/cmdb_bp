#encoding: utf-8
from flask import Blueprint

log = Blueprint('login',__name__, 
       template_folder='templates')
import views
