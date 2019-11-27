# -*- coding: UTF-8 -*-
import json as _json

# python object ->  JSON String
# dict	object
# list, tuple	array
# str, unicode	string
# int, long, float	number
# True	true
# False	false
# None	null
print(_json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], indent=4, sort_keys=True))

# JSON String -> python object
# object	dict
# array	list
# string	unicode
# number (int)	int, long
# number (real)	float
# true	True
# false	False
# null	None
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
print(_json.loads(jsonData))
map = _json.loads(jsonData)
print(map['a'])