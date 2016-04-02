from app import app, db
import os
from FormInfo import *
from random import randint
from Models import *
from image_getter import image_dem
import requests
from flask import render_template, request, url_for, redirect, jsonify, flash, session
db.create_all()


@app.route('/')
def root():
    return redirect(url_for('.login'))


@app.route("/login", methods=["POST", "GET"])
def login():
    login = LoginForm(csrf_enabled=False)
    user = Profile()
    if request.method == "POST":
        login.populate_obj(user)
        if login.validate_on_submit():
            if user.validate():
                session['username'] = user.username
                return redirect(url_for('.home'))
        flash("Password or Username INVALID")

    return render_template('login.html', form=login, formname='login')


@app.route("/signup", methods=["POST", "GET"])
def signup():
    user = Profile()
    register = RegisterForm(csrf_enabled=False)
    if request.method == "POST":
        register.populate_obj(user)
        if register.validate_on_submit():
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('.login'))
    return render_template('register.html', form=register, formname="register")


@app.route('/home')
def home():
    if session.has_key('username'):
        item = Item.query.filter_by(username=session['username']).all()
        return render_template('home.html', items=item)
    return redirect(url_for('.login'))


@app.route('/logout')
def logout():
    if session.has_key('username'):
        session.pop('username', None)
    return redirect(url_for('.login'))


@app.route('/thumburl', methods=['GET', 'POST'])
def thumbnail_url():
    if session.has_key('username'):
        form = UrlForm()
        if request.method == 'POST':
            url = request.form['url']
            session['images'] = image_dem(url)
            return redirect(url_for('.thumbnaillist'))
        return render_template('thumburl.html', form=form, formname="thumbnaillist")
    return redirect(url_for('.login'))


@app.route('/thumbnaillist')
def thumblist():
    if session.has_key('username'):
        images = session['images']
        session.pop('images', None)
        return render_template('thumbnaillist.html', images=images)
    return redirect(url_for('.login'))


@app.route('/addwish', methods=['GET', 'POST'])
def addwish():
    if session.has_key('username'):
        item = Item()
        addwish = ThumbnailForm(csrf_enabled=False)
        img_url = request.args.get('url')
        if img_url != None:
            addwish.url.data = img_url
        if request.method == 'POST':
            addwish.populate_obj(item)
            if addwish.validate_on_submit():
                item.username = session['username']
                item.thumbnail = get_thumbnail(item.url)
                db.session.add(item)
                db.session.commit()
                return redirect(url_for('.home'))
        return render_template('addwish.html', form=addwish, formname='addtowishlist')
    return redirect(url_for('.login'))


def get_thumbnail(url):
    thumbnailurl = url_for(
        'static', filename='img/thumbnail' + str(randint(0, 900)) + '.jpg')
    filepath = os.path.dirname(os.path.abspath(__file__)) + thumbnailurl
    f = open(filepath, 'wb')
    f.write(requests.get(url).content)
    f.close()
    return thumburl