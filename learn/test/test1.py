aa = {"data":{"fsdf":"fsdfsd", "dsa":"das1"}}
bb = {"dsa":"das3","dasdas":"dasd"}
print(dict(aa["data"], **bb))

del bb["dsa"]
print(bb.pop("dsa"))
print(bb)

# print(aa.get("das"))
# if aa.get("dd"):
#     print("dasd")

print("---")

if "dsa" not in bb:
    print("oooo")


ss = [1,2,34,54]
for i in ss:
    if "dsads" not in bb:
        print("ooo")
        continue
    print("inin")
