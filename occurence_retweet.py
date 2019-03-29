from elasticsearch import Elasticsearch
import csv

countlang = [[],[]]

es = Elasticsearch([{'host': 'mercure11.octopeek.com', 'port': 9200}])
res = es.search(index="twitter_festival_index",
                scroll = '2m',
                size = 1000,
                body=
                {
                  "query" : {
                    "match_phrase":{
                      "text":{
                        "query": "lollapalooza"
                      }
                    },
                    "filter" : {
                      "must" : {
                        "range":{
                          "favorite_count" : { "gt" : 100 } 
                        }
                      }   
                    }
                  }
                }
              )

print res