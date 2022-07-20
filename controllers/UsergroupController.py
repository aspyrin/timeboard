from flask import render_template, redirect, request
from models.Models import UserGroup
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def index():
    usergroups = UserGroup.query.order_by(UserGroup.name).all()
    return render_template("usergroups.html", usergroups=usergroups)


def create():
    if request.method == 'POST':
        name = request.form['name']
        usergroup = UserGroup(name=name)
        db.session.add(usergroup)
        db.session.commit()
        return redirect('/usergroups')
    else:
        return render_template("usergroup_create.html")


def detail(usergroup_id):
    if request.method == 'GET':
        usergroup = db.session.query(UserGroup).get(usergroup_id)
        return render_template("usergroup_detail.html", usergroup=usergroup)


def update(usergroup_id):
    usergroup = db.session.query(UserGroup).get(usergroup_id)
    if request.method == 'POST':
        usergroup.name = str(request.form['name'])
        db.session.commit()
        return redirect('/usergroups')
    else:
        return render_template("usergroup_update.html", usergroup=usergroup)


def delete(usergroup_id):
    usergroup = db.session.query(UserGroup).get(usergroup_id)
    db.session.delete(usergroup)
    db.session.commit()
    return redirect('/usergroups')
