from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import Required
from wtforms import StringField, TextAreaField, FileField, SubmitField

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True)
    hash_pass = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref = 'user', lazy = "dynamic")
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError("You cannot read password attribute")

    @password.setter
    def password(self, pass_entry):
        self.hash_pass = generate_password_hash(pass_entry)

    def verify_password(self, pass_entry):
        return check_password_hash(self.hash_pass, pass_entry)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id

    def __repr__(self):
        return f'User {self.username}::{self.id}'

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'blog', lazy = "dynamic")


    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_user_blogs(user_id):
        return Blog.query.filter_by(user_id = user_id).all()

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key= True)
    content = db.Column(db.String())
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))