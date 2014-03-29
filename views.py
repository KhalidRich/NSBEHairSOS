from flask import Flask, render_template, flash, redirect, session, url_for, request, g
#from flask.ext.SQLAlchemy import SQLAlchemy
import webapp2, models

app = Flask(__name__)
#db = SQLAlchemy(app)

@app.route("/")
def index():
  url_for('static', filename='css/bootstrap.css')
  return render_template('index.html')

@app.route("/user")
def user():
  url_for('static', filename='css/bootstrap.css')
#this should render the user sign up form
  return render_template('user.html')

@app.route("/professional")
def professional():
  url_for('static', filename="css/bootstrap.css")
#this should render the professional sign up form
  return render_template('professional.html')

@app.route("/search")
def search():
  url_for('static', filename="css/bootstrap.css")
#this should render the search page.
  return render_template

@app.route("/details/<professional_id>")
def details():
  url_for('static', filename="css/bootstrap.css")
  #this should render the details page for a stylist
  return render_template('details.html', profile=prof, reviews=rev)

@app.route("/about")
def about():
  url_for('static', filename="css/bootstrap.css")
  return render_template('about.html')

