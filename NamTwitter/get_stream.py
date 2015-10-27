#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twython import Twython
from flask import Flask, Response, json


#Flask app
app = Flask(__name__)


@app.route("/")
def init():

	#Get tweets by term
	results = getStream('#Ñam', 1000)

	#Returns a json format
	json = formatStream(results)	

	#Prin values in json, ready to use in javascript
	return Response(json,  mimetype='application/json')


#Setup to get Tweets
def setupStream():

	t = Twython(app_key='', 
	            app_secret='', 
	            oauth_token='', 
	            oauth_token_secret='')
	return t


#Returns tweets, we can add more functions, filters, etc.
def getStream(term, count):
	t = setupStream()
	result = t.search(q=term, count=count)
	return result


#Format and values to return
def formatStream(results):

	tweets = []	
	for t in results['statuses']:
		tweets.append(t)
  	return json.dumps(tweets)


#Init the app
if __name__ == '__main__':

	#Active debug
	app.debug = True

	app.run()