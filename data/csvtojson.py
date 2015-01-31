import csv
import json

csvfile = open('PERAB_Public_Comments.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("Time", "Name", "Organization", "Type of Organization", "Direct Your Comment", "Comment", "Filename")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
