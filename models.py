from google.appengine.ext import ndb

class User(ndb.Model):
  email = ndb.StringProperty()
  name = ndb.StringProperty()
  location = ndb.StringProperty()

class Stylist(ndb.Model):
  email = ndb.StringProperty()
  name = ndb.StringProperty()
  location = ndb.StringProperty()
  website = ndb.StringProperty()
  phone_number = ndb.StringProperty()
  open_hours = ndb.StringProperty()
  close_hours = ndb.StringProperty()
  days_open = ndb.IntegerProperty()
  desc = ndb.StringProperty()

class Review(ndb.Model):
  user = ndb.UserProperty()
  reviewed = ndb.UserProperty()
  rating = ndb.IntegerProperty()
  review = ndb.StringProperty()
  wait_time = ndb.IntegerProperty()
  cost = ndb.IntegerProperty()


