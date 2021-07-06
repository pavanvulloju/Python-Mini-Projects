import csv
import os
import json

marks_dict = {}
for a in os.listdir():
	if a !='marks_to_json.py' and a != 'marks.json' and not os.path.isdir(a):

		with open(a) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				try:
					marks_dict[row['RollNo']].append(row['CGPA'])
				except :
					marks_dict[row['RollNo']] = [row['CGPA']]


''' To know who left the college run this snippet'''
# left_clg = []
# for rno, data in marks_dict.items():
# 	if len(data) != 6:
# 		left_clg.append(rno)
# print(left_clg)


'''Can be used in future not used now just convert it to csv'''
with open('my_json_dir/marks.json', 'w') as json_file:
	json.dump(marks_dict, json_file, indent=4)
