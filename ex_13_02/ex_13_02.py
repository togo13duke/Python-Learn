import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location:")

if len(url) < 1 :
    url = "http://py4e-data.dr-chuck.net/comments_42.json"

print("Retrieving:", url)

urlhander = urllib.request.urlopen(url)
data = urlhander.read().decode()

print('Retrieved', len(data), 'characters')

try:
    jsdata = json.loads(data)
except:
    jsdata = None

comments = jsdata['comments']
print("Count:",len(comments))

sum = 0

for comment in comments:
    sum += int(comment['count'])

print("Sum:", sum)