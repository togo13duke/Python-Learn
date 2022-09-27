import json
import sqlite3
import urllib.request, urllib.parse, urllib.error

conn = sqlite3.connect('../databases/py4e.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

# url = input("Enter location:")
#
# if len(url) < 1 :
#     url = "https://www.py4e.com/tools/sql-intro/roster_data.json"
#
# print("Retrieving:", url)
#
# urlhander = urllib.request.urlopen(url)
# str_data = urlhander.read().decode()
#
# print('Retrieved', len(str_data), 'characters')

try:
    json_data = json.loads(str_data)
except:
    json_data = None

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title))

    cur.execute('''
    INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('''
    INSERT OR IGNORE INTO Course (title)
            VALUES ( ? )''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
            (user_id, course_id, role) VALUES ( ?, ?, ? )''',
                (user_id, course_id, role))

conn.commit()