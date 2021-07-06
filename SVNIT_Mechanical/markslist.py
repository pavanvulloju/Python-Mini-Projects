import os
import re

regex = 'U18ME.*?\n'

for a in os.listdir():
	if not os.path.isdir(a) and a != 'markslist.py':
		with open(f'./{a}', 'r') as f:
			data = f.read()

		with open(f'./CSV_Files/{a[:-4]}.csv', 'a') as g:
			g.write('RollNo,CGPA\n')
			for b in re.findall(regex, data):
				k = str(b).split(' ')
				roll_no = k[0]
				cgpa = k[2]
				line = roll_no + ',' + cgpa
				g.write(line)


