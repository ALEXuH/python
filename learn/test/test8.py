district = "dasd"
filter_str = "&area_district.name=eq.%s" % district
print(filter_str)


data = [
    {
        "count": 6,
        "executeDep": "城管执法局"
    },
    {
        "count": 1,
        "executeDep": "城管中队"
    },
    {
        "count": 1,
        "executeDep": "城管中队"
    }
]

data1 = []
map = {"街区工作站":["静安寺街道分中心"],"市容所":["市容所","规划资源局"],"城管中队":["城管中队", "城管执法局"],"管理办公室":["街道社区管理办公室","四明居民区"],"房管办事处":["建管委","华园物业","房管局"],"绿化所":["绿化市容局"],
       "党群工作办公室":["人保局", "12319", "12345市民服务热线", "信访办"],"公安派出所":["公安分局"],"市场监管所":["市场监管所"],
       "发展办公室":["投资办"],"服务办公室":["文化旅游局"],"环卫所":["生态环境局"]}
for i in data:
    dep = i["executeDep"]
    count = i["count"]
    value = {}
    for k,v in map.items():
        if dep in v:
            value["executeDep"] = dep
            value["count"] = count
            for j in data1:
                print("aa")
                dep1 = j["executeDep"]
                count1 = j["count"]
                if dep == dep1:
                    count2 = count + count1
                    print(count2)
                    j["count"] = count2
            data1.append(value)

print(data1)

data = []
for i in data:
    print("cc")
print(len(data))

data1 = {"dssa":"dsa","das":"dsadasd"}
print(",".join(data1.values()))

map = {}
map[",".join(data1.values())]["aa"] = 20
print(map)