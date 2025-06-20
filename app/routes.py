from app import app, db
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from flask import render_template, redirect, flash, url_for
from app.login import LoginForm
from app.models import User
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))