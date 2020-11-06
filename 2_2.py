# https://www.youtube.com/watch?v=Iu-HLy9hICg, 24:08
# normalizacja danych - polskie ogonki

import os
srcDir = os.getcwd() + "/Data/"
dstDir = os.getcwd() + "/Process/"

for fileName in os.listdir(srcDir):
	if fileName.endswith('txt'):
		try:
			srcFile = open(srcDir + fileName, 'r', encoding='UTF-8')
			text = srcFile.read()
		except UnicodeDecodeError:
			srcFile = open(srcDir + fileName, 'r', encoding='cp1250')
			text = srcFile.read()
		with open(dstDir + fileName, 'w', encoding='UTF-8') as dstFile:
			dstFile.write(text)
