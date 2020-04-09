
#from elasticsearch import Elasticsearch
from elasticsearch import Elasticsearch

index = "employee"
host = "localhost"
port = 9200
query = """
{
  "query":{
    "match_all": {}
  }
  , "size": 1
}
"""

es = Elasticsearch("http://localhost:9200")
o = es.search(index, query)
print(o["hits"]["total"])
if "hits" in o:
    hits = o["hits"]
    for hit in hits["hits"]:
        print(type(hit["_source"]))
        print(hit["_source"])

o = es.search(index, query, scroll="1h")
print(o)
for i in o:
    print(i)

print(o["_scroll_id"])
print(o["hits"]["hits"][0]["_source"])
print("------")
id = o["_scroll_id"]
es_out = es.scroll(scroll_id=id, scroll="1h")

for i in es_out:
    print(i)
print(es_out["hits"]["hits"][0]["_source"])
print(es_out["_scroll_id"])

es_out1 = es.scroll(scroll_id=id, scroll="1h")

for i in es_out1:
    print(i)
print(es_out1["hits"]["hits"][0]["_source"])
print(es_out1["_scroll_id"])

es_out2 = es.scroll(scroll_id=id, scroll="1h")

for i in es_out2:
    print(i)

print("====")
print(es_out2["hits"])
print(es_out2["_scroll_id"])
print("----------")
for i in o["hits"]:
    print(i)

print("---")
print(o["hits"]["total"])
print("---")
print(o["hits"]["hits"])

class a:
    def bigDataExecute(self, scroll="1h"):
        es = Elasticsearch(host="localhost", port=9200)
        query = query = """{
  "query":{
    "match_all": {}
  }
  ,"size": 10000
}"""
        o = es.search("employee", body=query, scroll='1h')
        print("---")
        print(o["hits"]["hits"])
        print(type(o["hits"]["hits"]))
        print("----")
        if "hits" in o:
            hits = o["hits"]
            for hit in hits["hits"]:
                yield hit["_source"]
        scroll_id = o["_scroll_id"]
        es_out = es.scroll(scroll_id=scroll_id, scroll="1h")
        hits = es_out["hits"]["hits"]
        print("----")
        print(hits)
        print("---")
        while len(hits) > 0:
            for hit in hits:
                yield hit["_source"]
            scroll_id = es_out["_scroll_id"]
            es_out = es.scroll(scroll_id=scroll_id, scroll="1h")
            hits = es_out["hits"]["hits"]

result = a().bigDataExecute()

for data in result:
    print(data)
