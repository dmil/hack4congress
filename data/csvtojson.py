import csv
import json

csvfile = open('PERAB_Public_Comments.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("Time", "Name", "Type of Organization", "Comment")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
  for i in range(1, 7):
    if i != 3 and i != 5 and i != 7:
      final_row = final_row + "," + row[i] + "\n"
    json.dump(final_row, jsonfile)
    jsonfile.write('\n')
