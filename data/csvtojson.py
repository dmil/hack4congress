import csv
import json

csvfile = open('1000-comments.csv', 'r')

fieldnames = ("Time", "Name", "Type of Organization", "Comment")
reader = csv.DictReader(csvfile)

rows = []
for row in reader:
  row = dict((key,value) for key, value in row.iteritems() if key == "Name" or key == "Comment")
  rows.append(row)


with open('file.json', 'w') as jsonfile:
  json.dump(rows, jsonfile, indent=2)
