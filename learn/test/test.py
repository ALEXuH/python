


# "str" % (args)
a = "cc"
b = "bb"
c = "xiao%s hong %s" %(a, b)
d = "xas%sda" % a

# "str{0} {1}".format(args)
e = "ad {0} asdd {1}".format(a, c)
print(e)
print(c)
print(d)

# join
f = ["dsa", "das", "dweq"]
print(a.join(","))
print(",".join(f))