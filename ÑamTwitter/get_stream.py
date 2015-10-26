from Twython import Twython


def setupStream():

	t = Twython(app_key='pTb3Yt82eTfa29l7P6HuHYGPh', 
	            app_secret='Ac9AIOOa0DrfJNZFQEPlkilqYIPTSCqpoUmWcbXppE5dKpWjWi', 
	            oauth_token='64845117-SNcgxtWaRJ4rbgnpWquLPicaL8vW6iA7U1qCUkxsw', 
	            oauth_token_secret='hVCkPcMCXZfiM7lFmErDkTqgqC2pANTij93zpLXOoqAnQ')
	return t


def getStream(term, count):
	t = setupStream()
	result = t.search(q=term, count=count)
	return result


def formatStream(result):

	data = []
	tweets = result['statuses']

	for tweet in tweets:
  		data.append(tweet['id_str'], tweet['text'])

	return data


if __name__ == '__main__':

	#Get tweets by term
	results = getStream('#Ñam', 1000)

	#Format results (JSON, CSV). Now is list
	data = formatStream(results)

	#Print results
	print data


