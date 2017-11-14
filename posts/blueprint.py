from flask import Blueprint, request
from flask import render_template

from models import Post, Tag
from .forms import PostForm

posts = Blueprint('posts', __name__, template_folder='templates')

#http://localhost/blog/create
@posts.route('/create')
def create_post():
    form = PostForm()
    return render_template('posts/create_post.html', form=form)

@posts.route('/') 
def index():

    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    else:
        posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)

@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)

# http://localhost/blog/tag/python
@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)