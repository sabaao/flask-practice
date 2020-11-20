from flask import Flask, redirect, url_for,request
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'hello world'

@app.route('/hello<name>')
def hello_name(name:str):
    return 'hello %s!' % name

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
if __name__ =='__main__':
    app.run()