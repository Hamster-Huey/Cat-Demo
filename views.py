from app import app
import os
from flask import send_from_directory

@app.route('/')
@app.route('/index')
def index():
  return send_from_directory('index', 'index.html')
  
@app.route('/hi')
def hi():
  try: lst = os.listdir('/tmp/test1/app/images')
  except OSError as err:
    return str(err)
  else:
    return str(len(lst))
  return '0'
  
@app.route('/images/<path:path>')
def images(path):
  return send_from_directory('/tmp/test1/app/images', path)