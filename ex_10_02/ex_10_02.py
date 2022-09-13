"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
>From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except:
    print("Invalid file name")

hour_dic = dict()

for line in handle:
    if not line.startswith("From "): continue
    line = line.rstrip()
    words = line.split()
    time = words[5]
    hour = time.split(":")[0]
    #print(time,hour)

    hour_dic[hour] = hour_dic.get(hour,0) + 1

hour_list = list()

for key,val in hour_dic.items():
    tup = (key,val)
    hour_list.append(tup)
    hour_list = sorted(hour_list,reverse=False)

for key,val in hour_list:
    print(key,val)





