import sqlite3
import re

db = sqlite3.connect("emaildb.sqlite")
cur = db.cursor()

cur.execute("Drop Table if exists Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

file = open("mbox.txt", "r")

for line in file:
  if (not re.search("^From: ", line)): continue
  email = re.findall("@([\w.-]+)", line.strip())
  mail = email[0]
  
  cur.execute('SELECT count FROM Counts WHERE org = ? ', (mail,))
  row = cur.fetchone()

  if (row == None):
    cur.execute("Insert into Counts (org, count) Values (?, 1)", (mail,))
  else:
    cur.execute("Update Counts Set count = count + 1 Where org = ?", (mail,))

db.commit()

# for row in cur.execute("Select * from Counts"):
#   print(str(row[0]), row[1])

cur.close()

