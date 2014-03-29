from views import db

class User(db.Model):
  _id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True)
  name = db.Column(db.String(51))
  location = db.Column(db.String(200))

class Stylist(db.Model):
  _id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True)
  name = db.Column(db.String(51))
  location = db.Column(db.String(200))
  website = db.Column(db.String(55))
  phone_number = db.Column(db.String(11))
  open_hours = db.Column(db.String(9))
  close_hours = db.Column(db.String(9))
  days_open = db.Column(db.Integer)
  desc = db.Column(db.String(255))

class Review(db.Model):
  _id = db.Column(db.Integer, primary_key=True)
  userid = db.Column(db.Integer, db.ForeignKey('user._id'))
  stylistid = db.Column(db.Integer, db.ForeignKey('stylist._id'))
  rating = db.Column(db.Integer)
  review = db.Column(db.String(255))
  wait_time = db.Column(db.Integer)
  cost = db.Column(db.Integer)


