import requests
import sys
import json
 
import authorization
from urls import *

def get_retweets(user_id):
	"""retrieve up to the last 100 tweets the from the user"""
	url = RETWEET_URL.format(user_id=user_id)
	response = requests.get(url)
	return response.text

def main():
	"""Main function"""
	authorization.authorize()
	retweets = get_retweets(sys.argv[1])
	print json.loads(retweets.json())
	'''
	keep getting AttributeError: 'unicode' object has no attribute 'json'
	'''
if __name__ == "__main__":
	main()

