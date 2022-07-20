from flask import render_template, redirect, request
from models.Models import Task
from flask_sqlalchemy import SQLAlchemy
from utils import str_to_date

db = SQLAlchemy()


def index():
    tasks = Task.query.order_by(Task.start_date).all()
    return render_template("tasks.html", tasks=tasks)


def create():
    if request.method == 'POST':
        title = request.form['title']
        category_id = int(request.form['category_id'])
        text = request.form['text']
        parent_task_id = int(request.form['parent_task_id'])
        target_user_id = int(request.form['target_user_id'])
        start_date = str_to_date(request.form['start_date'])
        end_date = str_to_date(request.form['end_date'])
        remind_date = str_to_date(request.form['remind_date'])
        creator_id = 1
        # changed = datetime.utcnow()
        last_changer_id = 1

        task = Task(category_id=category_id,
                    title=title,
                    text=text,
                    parent_task_id=parent_task_id,
                    target_user_id=target_user_id,
                    start_date=start_date,
                    end_date=end_date,
                    remind_date=remind_date,
                    creator_id=creator_id,
                    last_changer_id=last_changer_id)
        db.session.add(task)
        db.session.commit()
        return redirect('/tasks')
    else:
        return render_template("task_create.html")


def detail(task_id):
    if request.method == 'GET':
        task = db.session.query(Task).get(task_id)
        return render_template("task_detail.html", task=task)


def update(task_id):
    task = db.session.query(Task).get(task_id)
    if request.method == 'POST':
        task.category_id = int(request.form['category_id'])
        task.title = request.form['title']
        task.text = request.form['text']
        task.parent_task_id = int(request.form['parent_task_id'])
        task.target_user_id = int(request.form['target_user_id'])
        task.start_date = str_to_date(request.form['start_date'])
        task.end_date = str_to_date(request.form['end_date'])
        task.remind_date = str_to_date(request.form['remind_date'])
        task.last_changer_id = 1

        db.session.commit()
        return redirect('/tasks')
    else:
        return render_template("task_update.html", task=task)


def delete(task_id):
    task = db.session.query(Task).get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/tasks')
