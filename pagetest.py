# coding:utf8

from bottle import route, run, template,debug
import dbtest

# db=[]

@route('/')
@route('/p/<i>')
def index(i=0):
    # return template("<b>Hello {{name}}</b>! <iframe src='data:text/html;base64,PHNjcmlwdD5hbGVydChkb2N1bWVudC5kb21haW4pO2FsZXJ0KHdpbmRvdy5sb2NhdGlvbik7PC9zY3JpcHQ+'></iframe> <iframe src='data:text/html;base64,aHR0cDovL2ltZ3NyYy5iYWlkdS5jb20vZm9ydW0vcGljL2l0ZW0vZDlhYTg3MDAzYWYzM2E4NzdlNzViY2I0Yzc1YzEwMzg1MjQzYjU5My5qcGc=></iframe>'", name=name)
    # return template('lan')
    # print db
    # print type(i)
    return dbtest.get_page(int(i))
    # return "123"

@route('/test')
def test():
    # print template('lan')
    return template('lan')

dbtest.readfile()
# debug(True)
run(host='0.0.0.0', port=8080, reloader=True)
# run(host='0.0.0.0', port=8080)
