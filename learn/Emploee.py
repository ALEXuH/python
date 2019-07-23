class Emploee:
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.count += 1

    def total(self):
        print("count: " + str(self.count))



em = Emploee("alexuh", 2000)
print em.name
print em.salary
em.total()

# __foo__: 定义的是特殊方法，一般是系统定义名字
# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module impor
# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了

class A:
    def __init__(self):
        print "parent construct method"

    def parentMethod(self):
        print "parent method"

class B:
    def parentMethod1(self):
        print "parent method"

class C(A,B):
    __secrectCount = 1
    def __init__(self):
        print "child construct method"

    def parentMethod(self):
        print "child method"

    def getCount(self):
        self.__secrectFunction()
        return self.__secrectCount

    def __secrectFunction(self):
        print "i am secrect function"

c = C()
c.parentMethod()
c.parentMethod1()
print c.getCount()
print c._C__secrectCount