from flask import Flask, redirect, url_for,request, render_template
from flask.globals import session
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/hello')
def hello_world():
    return 'hello world'

@app.route('/hello/<name>')
def hello_name(name:str):
    return render_template('hello.html', name = name)

@app.route('/blog/<int:postID>')
def show_blog(postID:int):
    return 'postID is %d' % postID

@app.route('/admin')
def hello_admin():
    return 'hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest:str):
    return 'hello %s as guest' % guest

@app.route('/user/<name>')
def hello_user(name:str):
    if name =='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))

@app.route('/hello/getparam',methods=['GET'])
def hello_getparam():
    user = request.args.get('nm')
    return 'nm is %s' % user

@app.route('/get/session',methods = ['GET'])
def get_session():
    if 'username' in session :
        username = session['username']
        return 'Logined as %s' % username
    else:
        return 'You are not logged in session'

@app.route('/set/session/<username>')
def set_session(username:str):
    session['username'] = username
    return redirect(url_for('get_session'))

if __name__ =='__main__':
    app.run()