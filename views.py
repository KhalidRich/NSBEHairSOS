from flask import Flask, render_template, flash, redirect, session, url_for, request, g
app = Flask(__name__)

@app.route("/")
def index():
  url_for('static', filename='css/bootstrap.css')
  return render_template('index.html')

