from flask import Blueprint
from flask import render_template

from models import Post

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/') 
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)

@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    return render_template('posts/post_detail.html', post=post)