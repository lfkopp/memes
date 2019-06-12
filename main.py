import os

files = os.listdir()


images = ['jpg','jpeg','png']

with open('README.md', 'w+') as f:
	f.write('<span style="white-space:nowrap">')
	for file in files:
		if file.split('.')[-1] in images:
			f.write('<img src="'+str(file)+'" height=250>\n')
	f.write('</span>')




os.system('git add .')
os.system('git commit -m atualizando')
os.system('git pull')
os.system('git push')
