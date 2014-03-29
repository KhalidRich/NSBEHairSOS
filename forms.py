#!/usr/bin/python

from google.appengine.ext import ndb
from models import Stylist, Review
import webapp2

class FormsHandler():
	def __init__(self, request):
		self.request = request

	def add_professional(self):
		name = self.request.form['name']
		email = self.request.form['email']
		location = self.request.form['location']
		phone_number = self.request.form['phone_number']
		website = self.request.form['website']

		stylist = Stylist(name=name, email=email, location=location, phone_number=phone_number, website=website)
		stylist.put()

	def add_review(self):
		user = self.request.form['user']
		reviewed = self.request.form['reviewed']
		rating = self.request.form['rating']
		review = self.request.form['review']
		wait_time = self.request.form['wait_time']
		cost = self.request.form['cost']

		review = Review(user=user, reviewed=reviewed, rating=rating, review=review, wait_time=wait_time, cost=cost)
		review.put()