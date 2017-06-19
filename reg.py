from flask import Flask, render_template, session, request, redirect, flash
app=Flask(__name__)
app.secret_key="ThisKeyIsSecretSecret"

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
Name_REGEX = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/info',methods=['POST'])
def forminfo():
    session['email'] = request.form['email']
    session['first'] = request.form['first']
    session['last'] = request.form['last']
    session['password'] = request.form['password']
    session['confirmpass'] = request.form['confirmpass']

    if len(request.form['email']) <1:
        flash("Email cannot be empty!")
        print "1"
    elif len(request.form['first']) <1:
        flash("First Name cannot be empty!")
        print "2"
    elif len(request.form['last']) <1:
        flash("Last Name cannot be empty!")
        print "3"
    elif len(request.form['password']) <1:
        flash("Password cannot be empty!")
        print "4"
    elif len(request.form['confirmpass']) <1:
        flash("Password Confirmation cannot be empty!")
        return render_template('index.html')
        print "5"
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email")
        print "6"
    elif not Name_REGEX.match(request.form['first']):
        flash ("First Name can only contain letters")
        print "7"
    elif not Name_REGEX.match(request.form['last']):
        flash("Last Name can only contain letters")
        print "8"
    elif len(request.form['password']) <8:
        flash("Please enter a password with more than 8 characters!")
        return render_template('index.html')
        print "9"
    elif len(request.form['confirmpass']) <8:
        flash("Please confirm password is longer than 8 characters")
        print "10"
    elif request.form['password'] != request.form['confirmpass']:
        flash("Passwords do not match, please try again")
        print "11"
    else:
        flash("We have all your information, we will send you a confirmation email shortly!")
    return redirect('/')
    


app.run(debug=True)