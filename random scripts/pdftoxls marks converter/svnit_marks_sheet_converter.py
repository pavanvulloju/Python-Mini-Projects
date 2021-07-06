# SVNIT Marks Sheet Converter ( PDF to XlSX )

import re

regex = 'U1\dME.*?\n'

with open('./text.txt', 'r') as f:
	data = f.read()

with open('marks.csv', 'a') as g:
	for a in re.findall(regex, data):
		k = str(a).replace(' ', ',')
		g.write(k)


