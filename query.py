from elasticsearch import Elasticsearch
import csv

countfestival = [[],[]]

es = Elasticsearch([{'host': 'mercure11.octopeek.com', 'port': 9200}])
# res = es.search(index="twitter_groupe1_index", body={"query": {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total'])
# for hit in res['hits']['hits']:
#     print(hit["_source"])
res = es.search(index="twitter_festival_index",
                body=
                # search all 'rock en seine'
                {
                  "query" : {
                    "match":{
                      "text":{
                        "query": "rock en seine"
                      }
                    }
                  }
                }
              )

countfestival[0].append("rock en seine")
countfestival[1].append(res['hits']['total'])


res = es.search(index="twitter_festival_index",
                body=
                # search all 'lollapalooza'
                {
                  "query" : {
                    "match":{
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
                body=
                # search all 'tomorrowland'
                {
                  "query" : {
                    "match":{
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
                body=
                # search all 'solidays'
                {
                  "query" : {
                    "match":{
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
                body=
                # search all 'lowlands'
                {
                  "query" : {
                    "match":{
                      "text":{
                        "query": "lowlands"
                      }
                    }
                  }
                }
              )

countfestival[0].append("lowlands")
countfestival[1].append(res['hits']['total'])

print("HERE IS  mylist =>", countfestival)

f = open('output.csv', 'w')
with f:
  writer = csv.writer(f)

  for row in countfestival:
    writer.writerow(row)

