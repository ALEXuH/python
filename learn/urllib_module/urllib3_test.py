import urllib3
http = urllib3.PoolManager()
r = http.request("GET", "http://httpbin.org/robots.txt")
print(r.status)
print(r.data)
