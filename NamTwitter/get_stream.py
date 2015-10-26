#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twython import Twython


def setupStream():

	t = Twython(app_key='', 
	            app_secret='', 
	            oauth_token='', 
	            oauth_token_secret='')
	return t


def getStream(term, count):
	t = setupStream()
	result = t.search(q=term, count=count)
	return result


def formatStream(results):

	data = []
	tweets = results['statuses']

	for tweet in tweets:
  		data.append([tweet['id_str'], tweet['text']])

	return data


if __name__ == '__main__':

	#Get tweets by term
	results = getStream('#Ñam', 1000)

	#Format results (JSON, CSV). Now is list
	data = formatStream(results)

	#Print results
	print data


