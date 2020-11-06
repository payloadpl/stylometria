# https://www.youtube.com/watch?v=Iu-HLy9hICg, 23:30
# normalizacja danych - konwersja do formatu 'txt'

import os
import subprocess

dir = os.getcwd() + "/Data/"
for fileName in os.listdir("Data"):
	if fileName.endswith(('docx', 'rtf')):
		print(fileName)
		fileName = dir + fileName
		cmd = r'"C:\Program Files\LibreOffice\program\soffice.exe" --convert-to txt "{}" --outdir Data'.format(fileName)
		subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)

# nie wiadomo, co w oryginale było za "--outdir" - dopisaliśmy "z głowy", bez testowania - zobacz też poprawioną przez nas i przetestowaną na Linuksie wersję 2_1_linux.py
