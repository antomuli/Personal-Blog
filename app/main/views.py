from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from . import main
from sqlalchemy import desc
from ..models import Blog, User, Comment
from ..requests import get_quote
from ..forms import CommentForm, PostForm
from flask_login import login_required, current_user

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringaschool:anthonymuli8t@localhost/blog'


db = SQLAlchemy(app)


@main.route("/")
def index():
    
    quote = get_quote()
    return render_template("index.html", quote=quote)

@main.route('/blogs')
@login_required
def blogs():
    all_blogs = Blog.query.order_by(db.desc(Blog.created_at)).limit(15)

    return render_template('blogs.html', all_blogs=all_blogs)

@main.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).first()

    return render_template('post.html', post=post)

@main.route('/post')
def add():
    return render_template('post.html')

@main.route('/addblog', methods=['GET','POST'])
@login_required
def addpost():

    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        new_blog = Blog(title=title,
                        content=content, user=current_user)

        new_blog.save_blog()
        return redirect(url_for('main.index'))

    return render_template('new_blog.html', form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile.html", user=user)


@main.route('/post/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    blog = Blog.query.filter_by(id=id).first()

    if form.validate_on_submit():
        content = form.content.data

        new_comment = Comment(
            blog_id=blog.id, comments=content, user=current_user)

        new_comment.save_comment()
        print(new_comment)
        return redirect(url_for('main.index', id=post.id))

    return render_template('new_comment.html', comment_form=form)







if __name__ == '__main__':
    app.run(debug=True)