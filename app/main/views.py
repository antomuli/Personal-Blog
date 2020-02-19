from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from . import main
from sqlalchemy import desc
from ..models import Blog

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringaschool:anthonymuli8t@localhost/blog'


db = SQLAlchemy(app)


@main.route("/")
def index():
    all_blogs = Blog.query.order_by(db.desc(Blog.created_at)).limit(15).all()
    quote = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()['quote']
    print(quote)
    return render_template("index.html", blogs = all_blogs, quote = quote)
@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@main.route('/post')
def add():
    return render_template('post.html')

@main.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)