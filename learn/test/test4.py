class a:
    def test1(self, **kwargs):
        print("kwargs: {0}".format(kwargs))
        for k,v in kwargs.items():
            print("key: %s,value: %s" % (k, v))

    def test(self, *args):
        print("args: {0}".format(args))
        for i in  args:
            print("i: %s" % i)

    def test3(self, *args, **kwargs):
        for i in  args:
            print("i: %s" % i)
        print("----")
        for k,v in kwargs.items():
            print("key: %s,value: %s" % (k, v))

    def test4(self, name, *args, **kwargs):
        print("name: %s" % name)
        for i in  args:
            print("i: %s" % i)
        print("----")
        for k,v in kwargs.items():
            print("key: %s,value: %s" % (k, v))


dic = {"aa":"bb", "cc":"dasd","dsad":"dsadsd"}
arr = ["arr1", "arr2", "arr3"]
a = a()

# a.test("fsd",1,"fs",30)
# print("----")
# a.test(*arr)

#a.test1(**dic)
# a.test3(*arr, **dic)
# a.test3("432",a="cc",b="dd")
a.test4("alexuh", "das", "dd", **dic)
from bs4 import BeautifulSoup



