import urllib.request, urllib.parse, urllib.error
import json

service_url = "http://py4e-data.dr-chuck.net/json?"

address = input('Enter location: ')

if len(address) < 1:
    address = "South Federal University"

parms = dict()
parms['address'] = address
parms['key'] = 42

url = service_url + urllib.parse.urlencode(parms)

print("Retrieving:", url)

urlhander = urllib.request.urlopen(url)
data = urlhander.read().decode()

print('Retrieved', len(data), 'characters')

try:
    jsdata = json.loads(data)
except:
    jsdata = None

if not jsdata or 'status' not in jsdata or jsdata['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(jsdata)
    quit()

place_id = jsdata['results'][0]['place_id']
print("Place id",place_id)