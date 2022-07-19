from flask import Flask, render_template
from flask_migrate import Migrate

from models.Models import db

from routes.usergroup_bp import usergroup_bp
from routes.user_bp import user_bp
from routes.task_bp import task_bp
from routes.taskcategory_bp import taskcategory_bp

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(usergroup_bp, url_prefix='/usergroups')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(taskcategory_bp, url_prefix='/taskcategories')
app.register_blueprint(task_bp, url_prefix='/tasks')


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
