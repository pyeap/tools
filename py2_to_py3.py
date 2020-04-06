'''
convert python2 file to python3 file
'''

import os
import subprocess


def py2_to_py3(filedir):
	py_files = get_filelist(filedir)

	for pf in py_files:
		print(pf)
		cmd = '2to3 -w {}'.format(pf)
		subprocess.call(cmd, shell=True)


	

def get_filelist(dir):

	all_files = []
	for root, dirs, files in os.walk(dir):

		'''
		for dir in dirs:
			print(dir)
		'''
	
		for filename in files:
			fullname = os.path.join(root, filename)
			if fullname[-3:] == '.py':
				all_files.append(fullname)
				#print(fullname)
	return all_files
			
		



if __name__ == '__main__':
	py2_to_py3('./')