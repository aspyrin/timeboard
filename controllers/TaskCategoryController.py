from flask import render_template, redirect, request
from models.Models import TaskCategory
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def index():
    task_categories = TaskCategory.query.order_by(TaskCategory.title).all()
    return render_template("taskcategories.html", task_categories=task_categories)


def create():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        task_category = TaskCategory(title=title, desc=desc)
        db.session.add(task_category)
        db.session.commit()
        return redirect('/taskcategories')
    else:
        return render_template("taskcategory_create.html")


def detail(taskcategory_id):
    if request.method == 'GET':
        task_category = db.session.query(TaskCategory).get(taskcategory_id)
        return render_template("taskcategory_detail.html", task_category=task_category)


def update(taskcategory_id):
    task_category = db.session.query(TaskCategory).get(taskcategory_id)
    if request.method == 'POST':
        task_category.title = str(request.form['title'])
        task_category.desc = str(request.form['desc'])
        db.session.commit()
        return redirect('/taskcategories')
    else:
        return render_template("taskcategory_update.html", task_category=task_category)


def delete(taskcategory_id):
    task_category = db.session.query(TaskCategory).get(taskcategory_id)
    db.session.delete(task_category)
    db.session.commit()
    return redirect('/taskcategories')
