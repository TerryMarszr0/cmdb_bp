#encoding: utf-8
from flask import Blueprint

#app = Flask(__name__)
#app.secret_key = '\x11\x1fL\x931M\x16I\x8f\xddR\xc2jk\xe37\xdf\xbd\x8f\xd1\x9c\x9e\x1c\x1c\x89o\xc8\xa7\xf2\xe7H^'

user = Blueprint('user',__name__,
       template_folder='templates')
import views
