from flask import Flask
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

if __name__ =='__main__':
    app.run()