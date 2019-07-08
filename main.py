from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask (__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('index.html', title="Signin Page")
    
@app.route('/', methods=['POST'])

def validate_entry():

    username = request.form['user']
    password = request.form['password']
    verifypass = request.form['verify']
    email = request.form['email']

    error_user=''
    error_pass=''
    error_verify=''
    error_email=''

    if username == '':
        error_user = 'User name required'
    if password == '':
        error_pass = 'Password required'
    if verifypass == '':
        error_verify = 'Password verification required'
    if verifypass == '' and password == '':
        error_verify = 'Password required'



    return render_template('index.html', title="Error",
        style='.error { color: red; }',
        username=username,
        error_user=error_user,
        error_pass=error_pass,
        error_verify=error_verify,
        error_email=error_email)

@app.route('/welcome')
def welcome():
    user = request.args.get('user')
    return render_template('welcome.html', title='Welcome',
    user=user)

app.run()