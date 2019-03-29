from elasticsearch import Elasticsearch
import csv

countfestival = [[],[]]

es = Elasticsearch([{'host': 'mercure11.octopeek.com', 'port': 9200}])
# res = es.search(index="twitter_groupe1_index", body={"query": {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total'])
# for hit in res['hits']['hits']:
#     print(hit["_source"])
res = es.search(index="twitter_festival_index",
                scroll = '2m',
                size = 1000,
                body=
                # search all 'lollapalooza'
                {
                  "query" : {
                    "match_phrase":{
                      "text":{
                        "query": "lollapalooza"
                      }
                    }
                  }
                }
              )

countfestival[0].append("lollapalooza")
countfestival[1].append(res['hits']['total'])

res = es.search(index="twitter_festival_index",
                scroll = '2m',
                size = 1000,
                body=
                # search all 'tomorrowland'
                {
                  "query" : {
                    "match_phrase":{
                      "text":{
                        "query": "tomorrowland"
                      }
                    }
                  }
                }
              )

countfestival[0].append("tomorrowland")
countfestival[1].append(res['hits']['total'])

res = es.search(index="twitter_festival_index",
                scroll = '2m',
                size = 1000,
                body=
                # search all 'solidays'
                {
                  "query" : {
                    "match_phrase":{
                      "text":{
                        "query": "solidays"
                      }
                    }
                  }
                }
              )

countfestival[0].append("solidays")
countfestival[1].append(res['hits']['total'])

res = es.search(index="twitter_festival_index",
                scroll = '2m',
                size = 1000,
                body=
                # search all 'lowlands'
                {
                  "query" : {
                    "match_phrase":{
                      "text":{
                        "query": "lowlands"
                      }
                    }
                  }
                }
              )

countfestival[0].append("lowlands")
countfestival[1].append(res['hits']['total'])


res = es.search(index="twitter_festival_index",
                scroll = '2m',
                size = 1000,
                body=
                # search all 'hellfest'
                {
                  "query" : {
                    "match_phrase":{
                      "text":{
                        "query": "hellfest"
                      }
                    }
                  }
                }
              )
countfestival[0].append("hellfest")
countfestival[1].append(res['hits']['total'])  


res = es.search(index="twitter_festival_index",
                scroll = '2m',
                size = 1000,
                body=
                # search all 'summerfest'
                {
                  "query" : {
                    "match_phrase":{
                      "text":{
                        "query": "summerfest"
                      }
                    }
                  }
                }
              )

countfestival[0].append("summerfest")
countfestival[1].append(res['hits']['total'])

res = es.search(index="twitter_festival_index",
                scroll = '2m',
                size = 1000,
                body=
                # search all 'coachella'
                {
                  "query" : {
                    "match_phrase":{
                      "text":{
                        "query": "coachella"
                      }
                    }
                  }
                }
              )

countfestival[0].append("coachella")
countfestival[1].append(res['hits']['total'])

print("HERE IS  mylist =>", countfestival)

f = open('occurence_festival.csv', 'w')
with f:
  writer = csv.writer(f)

  for row in countfestival:
    writer.writerow(row)

