from flask import Blueprint
from controllers.TaskController import index, create, detail, update, delete


task_bp = Blueprint('task_bp', __name__)
task_bp.route('/', methods=['GET'])(index)
task_bp.route('/create', methods=['POST', 'GET'])(create)
task_bp.route('/<int:task_id>', methods=['GET'])(detail)
task_bp.route('/<int:task_id>/update', methods=['POST', 'GET'])(update)
task_bp.route('/<int:task_id>/delete', methods=['GET'])(delete)
