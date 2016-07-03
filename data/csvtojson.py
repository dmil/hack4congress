import csv
import json


with open('data/1000-comments-correct.csv', 'r') as csvfile: 
  reader = csv.DictReader(csvfile)

  rows = []
  for row in reader:
    row = dict((key,value) for key, value in row.iteritems() if key == "Name" or key == "Comment")
    rows.append(row)


with open('data/comment.json', 'w') as jsonfile:
  json.dump(rows, jsonfile, indent=2)
