from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class UserGroup(db.Model):
    """
    Model describe user-group
    """
    __tablename__ = 'usergroup'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return '<User group %r>' % self.name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class User(db.Model):
    """
    Model describe user-object
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    nick = db.Column(db.String(12))
    tg = db.Column(db.String)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    pw = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'nick': self.nick,
            'tg': self.tg,
            'email': self.email,
            'phone': self.phone,
            'pw': self.pw
        }


class TaskCategory(db.Model):
    """
    Model describe task-category object
    """
    __tablename__ = 'taskcategory'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    desc = db.Column(db.Text)

    def __repr__(self):
        return '<Task category %r>' % self.title

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'desc': self.text
        }


class Task(db.Model):
    """
    Model describe task-object
    """
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('taskcategory.id'))  #one-to-one
    category = db.relationship('TaskCategory', backref=db.backref('tasks_by_category', lazy=True))
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.Text)
    parent_task_id = db.Column(db.Integer)  # in future one-to-one
    target_user_id = db.Column(db.Integer)  # in future many-to-many
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    remind_date = db.Column(db.DateTime)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    changed = db.Column(db.DateTime, onupdate=datetime.utcnow)

    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # one-to-one
    creator = db.relationship('User', foreign_keys=[creator_id])

    last_changer_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # one-to-one
    last_changer = db.relationship('User', foreign_keys=[last_changer_id])

    def __repr__(self):
        return '<Task %r>' % self.title

    @property
    def serialize(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'title': self.title,
            'text': self.text,
            'parent_task_id': self.parent_task_id,
            'target_user_id': self.target_user_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'remind_date': self.remind_date,
            'created': self.created,
            'creator': self.creator,
            'changed': self.changed,
            'last_changer': self.last_changer,
        }
