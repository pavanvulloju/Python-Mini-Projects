import csv
import json


with open('./marks.json') as f:
	data = json.load(f)

with open('markslist.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["RollNo", "Sem-1", "Sem-2", "Sem-3", "Sem-4", "Sem-5", "Sem-6"])
	for key, val in data.items():
		if len(val) == 6:
			writer.writerow([key, val[0], val[1], val[2], val[3], val[4], val[5]])
