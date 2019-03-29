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
                        "query": "tomorrowland"
                      }
                    }
                  }
                }
              )

countEn = 0
countFr = 0
countEs = 0
countNl = 0
countPt = 0
countKo = 0

for item in res['hits']['hits']:
   if item['_source']["user"]["lang"] == "en" or item['_source']["user"]["lang"] == "en-gb":
    countEn += 1

   if item['_source']["user"]["lang"] == "fr":
     countFr += 1

   if item['_source']["user"]["lang"] == "es":
     countEs += 1

   if item['_source']["user"]["lang"] == "nl":
     countNl += 1

   if item['_source']["user"]["lang"] == "pt":
     countPt += 1


countlang[0].append("Anglais")
countlang[1].append(countEn)

countlang[0].append("Francais")
countlang[1].append(countFr)

countlang[0].append("Espagnol")
countlang[1].append(countEs)

countlang[0].append("Netherlands")
countlang[1].append(countNl)

countlang[0].append("Portuguais")
countlang[1].append(countPt)



f = open('lang_tomorrowland.csv', 'w')
with f:
  writer = csv.writer(f)

  for row in countlang:
    writer.writerow(row)