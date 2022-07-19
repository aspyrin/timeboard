from flask import Blueprint
from controllers.UsergroupController import index, create, detail, update, delete


usergroup_bp = Blueprint('usergroup_bp', __name__)
usergroup_bp.route('/', methods=['GET'])(index)
usergroup_bp.route('/create', methods=['POST', 'GET'])(create)
usergroup_bp.route('/<int:usergroup_id>', methods=['GET'])(detail)
usergroup_bp.route('/<int:usergroup_id>/update', methods=['POST', 'GET'])(update)
usergroup_bp.route('/<int:usergroup_id>/delete', methods=['GET'])(delete)
