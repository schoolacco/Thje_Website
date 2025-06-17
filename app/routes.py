from app import app
from flask import render_template, redirect, flash, url_for
from app.login import LoginForm
@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')
@app.route('/contact')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')
@app.route('/test')
@app.route('/test.html')
def test():
    user = {'username': 'real user'}
    return render_template('test.html', title= 'Test', user=user)
@app.route('/login')
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)