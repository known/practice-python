from flask import Flask, request, redirect, url_for, session, escape
from werkzeug import secure_filename

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    if 'username' in session:
        return '<h1>Hello %s!</h1>' % escape(session['username'])
    return '<h1>Hello World!</h1>'

@app.route('/hello/<user>')
def hello(user):
    return '<h1>Hello %s!</h1>' % user

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        if username == 'admin':
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'Login failure!'
    
    return '''
    <h1>Login</h1>
    <form action="/login" method="post">
        <p><input name="username" /></p>
        <p><button>Login</button></p>
    </form>
    <p>%s</p>''' % error

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['thefile']
        f.save('d:\\' + secure_filename(f.filename))
        return '<h1>Upload successful!</h1>'
    else:
        return '''
        <h1>Upload</h1>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <p><input type="file" name="thefile" /></p>
            <p><button>Upload</button></p>
        </form>'''

if __name__ == '__main__':
    app.run()
