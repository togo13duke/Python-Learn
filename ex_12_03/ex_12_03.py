import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter URL- ")
count = input("Enter count- ")
position = input("Enter positon -")
if len(url) < 1 :
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

cnt = 0
while cnt <= int(count):
    if cnt != 0:
        url = links[int(position) - 1].get("href")

    print("Retrieving:",url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("a[href]")

    cnt += 1
