# pip install jmespath
import jmespath
import source as s
import json as _json

print(jmespath.search("a", s.source))
print(jmespath.search("a.b.c", s.source))
print(jmespath.search("a.b.c[1]", s.source))
print(jmespath.search("a.b.c[0].d[1][0]", s.source1))
print(jmespath.search("a.b.c[0].d[0:2]", s.source1))
print(jmespath.search("[1:3]", s.source2))

print(jmespath.search("people[*].first", s.source3))
print(jmespath.search("people[1:2].first", s.source3))
print(jmespath.search("ops.*.numArgs", s.source4))
print(jmespath.search("reservations[*].instances[*]", s.source5))
print(jmespath.search("reservations[*].instances[*].state", s.source5))
print(jmespath.search("reservations[*].instances[*].*[][]", s.source5)) # flatMap []

print(jmespath.search("machines[?state=='running']", s.source6))
print(jmespath.search("machines[?state=='running'] | [].name", s.source6))

print(jmespath.search("people[].[name, state.name]", s.source7))
print(jmespath.search("people[?age >= `25`].{age1:age, name1:name}", s.source8))

print(jmespath.search("sort_by(Contents, &Size)[*].{KEY:Key, SIZE: Size}", s.source9))
print(jmespath.search("sort_by(Contents, &Date)[*].{KEY:Key, SIZE: Size}", s.source9))

print(jmespath.search("locations[?state == 'WA'].name | sort(@)[-2:] | {WashingtonCities: join(', ', @)}", s.source10))


a = jmespath.search("hits.hits[*]._source", s.source11)
with open("./aa.txt", "wb") as fd:
    for v in a:
        print(v)
        fd.write(_json.dumps(v))
        fd.write("\n")