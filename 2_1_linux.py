# https://www.youtube.com/watch?v=Iu-HLy9hICg, 23:30
# normalizacja danych - konwersja do formatu 'txt'

import os
import subprocess

dir = os.getcwd() + "/Data/"
for fileName in os.listdir("Data"):
	destFile = dir + fileName + ".txt"
	fileName = dir + fileName

	if fileName.endswith('rtf'):
		cmd = r'unrtf --nopict --noremap --text "{}" > "{}"'.format(fileName, destFile)
		subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)

	if fileName.endswith('doc'):
		cmd = r'timelimit -t5 -T3 catdoc "{}" > "{}"'.format(fileName, destFile)
		subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)

	if fileName.endswith('xls'):
		cmd = r'timelimit -t5 -T3 xls2csv "{}" > "{}"'.format(fileName, destFile)
		subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)

	if fileName.endswith('pdf'):
		cmd = r'pdftotext -layout -nopgbrk "{}" "{}"'.format(fileName, destFile)
		subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)

# podobny sposob mona sobie dopisac obsluge innych formatow, np. Office 2007+, html itd.
