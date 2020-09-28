from bottle import route, run, template, static_file
from bottle import TEMPLATE_PATH
import os

TEMPLATE_PATH.append("./view")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'view')

@route('/view/css/<filename:path>')
def send_static(filename):
    """静的ファイルを返す
    """
    return static_file(filename, root=f'{STATIC_DIR}/css')



@route('/')
def index():
	title="aaaa"
	return template('index_e.html',title=title)

@route('/', method='POST')
def index2():
	return template("index2.html")



run(host='localhost', port=8080)
