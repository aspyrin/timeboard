from flask import render_template, redirect, request
from models.Models import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def index():
    users = User.query.order_by(User.name).all()
    return render_template("users.html", users=users)


def create():
    if request.method == 'POST':
        name = request.form['name']
        nick = request.form['nick']
        tg = request.form['tg']
        email = request.form['email']
        phone = request.form['phone']
        pw = request.form['pw']
        user = User(name=name, nick=nick, tg=tg, email=email, phone=phone, pw=pw)
        db.session.add(user)
        db.session.commit()
        return redirect('/users')
    else:
        return render_template("user_create.html")


def detail(user_id):
    if request.method == 'GET':
        user = db.session.query(User).get(user_id)
        return render_template("user_detail.html", user=user)


def update(user_id):
    user = db.session.query(User).get(user_id)
    if request.method == 'POST':
        user.name = str(request.form['name'])
        user.nick = str(request.form['nick'])
        user.tg = str(request.form['tg'])
        user.email = str(request.form['email'])
        user.phone = str(request.form['phone'])
        user.pw = str(request.form['pw'])
        db.session.commit()
        return redirect('/users')
    else:
        return render_template("user_update.html", user=user)


def delete(user_id):
    user = db.session.query(User).get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')
