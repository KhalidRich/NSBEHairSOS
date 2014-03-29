from flask import Flask, render_template, flash, redirect, session, url_for, request, g
#from flask.ext.SQLAlchemy import SQLAlchemy
import webapp2, models, yelp, json
from google.appengine.api import users
from forms import FormsHandler

app = Flask(__name__)
#db = SQLAlchemy(app)

user = users.create_login_url()
sign_in_url = users.create_login_url()
sign_out_url = users.create_logout_url("/")

def check_for_logged_in():
  user = users.get_current_user()
  if user:
    return user
  else:
    return render_template('index.html', msg="You need to sign in to access other pages", url=users.create_login_url())

@app.route("/")
def index():
  url_for('static', filename='css/bootstrap.css')
  return render_template('index.html', sign_in_url=sign_in_url, sign_out_url=sign_out_url, user=users.get_current_user())

@app.route("/user")
def user():
  url_for('static', filename='css/bootstrap.css')
#this should render the user sign up form
  return render_template('user.html')

@app.route("/professional", methods=["GET", "POST"])
def professional():
  url_for('static', filename="css/bootstrap.css")

  if request.method == "POST":
    forms_handler = FormsHandler(request)
    forms_handler.add_professional()
#this should render the professional sign up form
  return render_template('professional.html')

@app.route("/maps", methods=["GET", "POST"])
def search():
  check_for_logged_in()
  if request.method == "POST":
    location = request.form['location']
    results = yelp.search("barber shop", location)
    return render_template('maps.html', results=json.dumps(results, ensure_ascii=False), location=location)
  url_for('static', filename="css/bootstrap.css")
#this should render the search page.
  return render_template('search.html', user=user, sign_in_url=sign_in_url, sign_out_url=sign_out_url)

@app.route("/details/<professional_id>")
def details():
  url_for('static', filename="css/bootstrap.css")
  #this should render the details page for a stylist
  return render_template('details.html', profile=prof, reviews=rev, sign_in_url=sign_in_url, sign_out_url=sign_out_url, user=user)

@app.route("/about")
def about():
  url_for('static', filename="css/bootstrap.css")
  return render_template('about.html', sign_in_url=sign_in_url, sign_out_url=sign_out_url,user=user)

