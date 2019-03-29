import tweepy
import sys
import json
from tweepy import OAuthHandler
from textwrap import TextWrapper
from datetime import datetime
from elasticsearch import Elasticsearch

consumer_key = "IzoLF82wVRoCinEvJIH40hzpp"
consumer_secret = "kPBeCQHNRmoknVDKCKqnpD7HCRm9O9XGIdJ17eatHgigN3EFu9"
access_token = "1108762221805481984-GinqHeokvFNBoytVyfSsASPYQuZcD7"
access_token_secret = "Y5hAOjGyOMKBYERH1HXyLP7pgIKUsFMSyghTcQQqhatX2"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


es = Elasticsearch([{'host': 'mercure11.octopeek.com', 'port': 9200}])
es.indices.create(index='twitter_festival_index', ignore=400)


class StreamApi(tweepy.StreamListener):
  status_wrapper = TextWrapper(width=60, initial_indent='   ', subsequent_indent='    ')

  def on_status(self, status):

    print 'n%s %s' % (status.author.screen_name, status.created_at)

    json_data = status._json
    print json_data['text']
    # with open('data.json', 'w') as outfile:
    #   json.dump(json_data, outfile)
    es.index(index="twitter_festival_index",
              doc_type="twitter",
              body=json_data,
              ignore = 400
            )


streamer = tweepy.Stream(auth=auth, listener=StreamApi())

terms = ['tomorrowland', 'solidays', 'lowlands', 'hellfest', 'lollapalooza', 'summerfest', 'coachella']

streamer.filter(None, terms)