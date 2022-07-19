from flask import Blueprint
from controllers.TaskCategoryController import index, create, detail, update, delete


taskcategory_bp = Blueprint('taskcategory_bp', __name__)
taskcategory_bp.route('/', methods=['GET'])(index)
taskcategory_bp.route('/create', methods=['POST', 'GET'])(create)
taskcategory_bp.route('/<int:taskcategory_id>', methods=['GET'])(detail)
taskcategory_bp.route('/<int:taskcategory_id>/update', methods=['POST', 'GET'])(update)
taskcategory_bp.route('/<int:taskcategory_id>/delete', methods=['GET'])(delete)
