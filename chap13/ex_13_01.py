import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter location:")

if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.xml"

print("Retrieving:", url)

xml = urllib.request.urlopen(url).read()
tree = ET.fromstring(xml)

print('Retrieved', len(xml), 'characters')

counts = tree.findall('.//count')

print('Count:', len(counts))

sum = 0
for count in counts:
    sum += int(count.text)

print("Sum:", sum)
