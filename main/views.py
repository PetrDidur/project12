from flask import Blueprint, render_template, request
from main.utils import PostHandler
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', static_folder='static')

@main_blueprint.route('/')
def index_page():
    return render_template('index.html')

@main_blueprint.route('/search/')
def search_page():
    substr = request.args.get('s')
    post_handler = PostHandler('posts.json')
    posts = post_handler.search_posts(substr)
    return render_template('post_list.html', posts=posts, substr=substr)

