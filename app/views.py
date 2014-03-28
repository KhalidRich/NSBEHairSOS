from flask import render_template, flash, redirect, session, url_for, request, g
from app import app

@app.route("/")
def index():
  return "This is our homepage"

