import requests
r = requests.get('https://api.github.com/events')
print type(r)

#print dir(r)
a = r.json();

#print a
try:
    for i in a:
        print "user's id login", i['actor']['login']
except:
    print "error"
