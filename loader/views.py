from flask import Blueprint, render_template

import app

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', static_folder='static')

@loader_blueprint.route('/post/')
def create_post_page():
    return render_template('/post_form.html')