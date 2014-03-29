import rauth
import time

def search(store_type, location):
	#locations = [(39.98,-82.98),(42.24,-83.61),(41.33,-89.13)]
	api_calls = []
	results = []
	#for lat,long in locations:
	params = getTopBarbers('barber shop',location)
	api_calls.append(get_results(params))

	print api_calls[0][u'businesses'][0]



	for b in api_calls[0][u'businesses']:
		{"name": b[u'name'], "address": ' '.join(b[u'location'][u'display_address'])}
	return api_calls

def getTopBarbers(store_type, addr):
	#See the Yelp API for more details
	params = {}
	params["term"] = store_type
	params["location"] = addr
	params["radius_filter"] = "40000"
	params["sort"] = 2;
	return params

def get_results(params):

	#Obtain these from Yelp's manage access page
  	consumer_key = "Um__FlVUdjQ0k7krsp4gng"
	consumer_secret = "WkIlFun9z-M4S2QBok7FZt4tViY"
	token = "flXNU9V16GdnnUKlSfAW5LSbecAkiONq"
	token_secret = "JwO2BzJR3KhfzB4akNEyhliIk4E"
	
	session = rauth.OAuth1Session(
		consumer_key = consumer_key
		,consumer_secret = consumer_secret
		,access_token = token
		,access_token_secret = token_secret)
		
	request = session.get("http://api.yelp.com/v2/search",params=params)
	
	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	session.close()
	
	return data
		
def get_search_parameters(lat,long):
	#See the Yelp API for more details
	params = {}
	params["term"] = "restaurant"
	params["ll"] = "{},{}".format(str(lat),str(long))
	params["radius_filter"] = "2000"
	params["limit"] = "10"

	return params

if __name__=="__main__":
	main()
