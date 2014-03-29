from flask import Flask, render_template, flash, redirect, session, url_for, request, g
app = Flask(__name__)

@app.route("/")
def index():
  return "This is our homepage"

