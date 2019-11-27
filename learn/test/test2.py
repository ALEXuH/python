list1 = ['html', 'js', 'css', 'python']
print(list1(range(1,5)))
list1 =list(range(10))
print(list1)
for i in list1[1:len(list1)]:
    print(i)
l = [1,2,3,4,5]
x = l.__iter__()
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())

print("----")
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
try:
    while True:
        print(x.next())
        print(",")

except:
    print("----")


while x.next():
    try:
        print(x.next())
    finally:
        print("]")
    print(",")

class a:
    def test(self):
        l = [1,2,3,4,5]
        b = 0
        for i in l:
            if b == 0:
                print(i)
            else:
                print(".")
                print(i)
            b += 1
a().test()