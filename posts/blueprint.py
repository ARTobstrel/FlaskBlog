from flask import Blueprint, request, redirect, url_for
from flask import render_template

from app import db
from models import Post, Tag
from .forms import PostForm

posts = Blueprint('posts', __name__, template_folder='templates')

#http://localhost/blog/create
@posts.route('/create', methods=['POST', 'GET'])
def create_post():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Something wrong')

        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)

@posts.route('/') 
def index():

    q = request.args.get('q')

    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)) #.all() #Отображает только те посты которые указаны в поиске
    else:
        posts = Post.query.order_by(Post.created.desc()) #Фильтрует отображение постов снизу на верх (сверху самые свежие)

    pages = posts.paginate(page=page, per_page=5)

    return render_template('posts/index.html', pages=pages)

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