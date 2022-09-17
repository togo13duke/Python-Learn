import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter - ")
if len(url) < 1 :
    url = "http://py4e-data.dr-chuck.net/comments_42.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all("span")

sum = 0
count = 0
for tag in tags:
    sum += int(tag.text)
    count += 1

print("count:",count)
print("sum:",sum)