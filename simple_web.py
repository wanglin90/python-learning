# -*- coding: utf-8 -*-

# flask are required

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return '<h1>Home</h1>'


@app.route('/signin',methods=['GET'])
def signin_form():
    return '''
        <form action='/signin' method='post'>
            <p><input name='username'></input></p>
            <p><input name='password' type='password'></input></p>
            <p><input type='submit'></input></p>
        </form>
    '''
@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h2> Hello admin </h2>'
    return '<h2> Bad request </h2>'

if __name__ == '__main__':
    app.run('127.0.0.1',8080)



