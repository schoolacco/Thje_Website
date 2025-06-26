from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from flask import render_template, redirect, flash, url_for, request
from urllib.parse import urlsplit
from app.forms import LoginForm, RegistrationForm
from app.models import User
@app.route('/')
@app.route('/index')
@app.route('/index.html')
@login_required
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
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
@app.route('register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)