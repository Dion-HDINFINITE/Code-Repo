from flask import Flask, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ILOVEYOU3000'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#FLASK ORM - SQLAlchemy
class User(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True, nullable=False)
	email = db.Column(db.String(200), unique=True, nullable=False)
	image_file = db.Column(db.String(100), nullable=False, default='default.jpg')
	password = db.Column(db.String(100), nullable=False)

	tweets = db.relationship('Tweet', backref='author', lazy=True)


class Tweet(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#FLASK FORM
class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


tweets = [
	{
		'author' : 'Budi Doremi',
		'content' : 'This is my first tweet',
		'date_posted' : 'May 10, 2022'
	},
	{
		'author' : 'Alex Chandra',
		'content' : 'Hello World',
		'date_posted' : 'May 11, 2022'
	}
]


@app.route("/") # 127.0.0.1:8000
@app.route("/home") # 127.0.0.1:8000/home
def home():
	return render_template('home.html', tweets=tweets)

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f"Account created for {form.username.data}!", "success")
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

@app.route("/about")
def about():
	return render_template('about.html', title='About Us')


if __name__ == '__main__':
	app.run(debug=True)




