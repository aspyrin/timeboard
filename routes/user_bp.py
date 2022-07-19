from flask import Blueprint
from controllers.UserController import index, create, detail, update, delete


user_bp = Blueprint('user_bp', __name__)
user_bp.route('/', methods=['GET'])(index)
user_bp.route('/create', methods=['POST', 'GET'])(create)
user_bp.route('/<int:user_id>', methods=['GET'])(detail)
user_bp.route('/<int:user_id>/update', methods=['POST', 'GET'])(update)
user_bp.route('/<int:user_id>/delete', methods=['GET'])(delete)
