import os

files = os.listdir()


images = ['jpg','jpeg','png']

with open('README.md', 'w+') as f:
	f.write('<span style="white-space:nowrap">')
	for file in files:
		if file.split('.')[-1] in images:
			f.write('<img src="'+str(file)+'" width=100>\n')
	f.write('</span')