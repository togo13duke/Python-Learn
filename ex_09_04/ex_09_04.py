"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except:
    print("Invalid file name")


dic = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith("From ") : continue    
    words = line.split()
    
    dic[words[1]] = dic.get(words[1],0) + 1

bigmail = None
bigcount = None

for email,send_count in dic.items():
    if bigmail is None or send_count > bigcount:
        bigmail = email
        bigcount = send_count

print(bigmail,bigcount)


