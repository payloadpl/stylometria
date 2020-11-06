# https://www.youtube.com/watch?v=Iu-HLy9hICg, 28:38
# podobienstwo (statystyczne wlasnosci) - wyliczanie wskaznikow

def GetSentences(text):
	return [s.strip() for s in re.split('[\.\?\!]', text)]

def GetWords(text):
	return re.split('\W+', text)

def GetPunctuations(text):
	return "".join(re.findall(r'[' + string.punctuation + ']', text))

def GetByteNGrams(text, n):
	return [text[i:i+n] for i in range(0, len(text)-n+1)]

def GetWordNGram(words, n):
	# tu w prezentacji byl blad - poprawilismy dla Was :)
	return [" ".join(words[i:i+n]) for i in range(0, len(words)-n+1)]


import os
import re
import string
from collections import Counter

dir = os.getcwd() + "/Process/"
data = {}
wordNGram = 2
byteNGram = 4

for fileName in os.listdir(dir):
	with open(dir + fileName, 'r', encoding='UTF-8') as srcFile:
		item = {}
		text = srcFile.read().lower()
		item["text"] = text

		# podzial na zdania
		item["sentences"] = GetSentences(text)
		# podzial na wyrazy
		item["words"] = GetWords(text)
		# wszystkie uzyte znaki interpunkcyjne
		item["punctuations"] = GetPunctuations(text)
		# bajtowe n-gramy
		item["byteNGrams"] = GetByteNGrams(text, byteNGram)
		# slowne n-gramy
		item["wordNGrams"] = GetWordNGram(item["words"], wordNGram + 1)

		data[fileName] = item


measure = {}
for key in data:
	item = {}

	# srednia dlugosc zdania
	item["avgSentences"] = len(data[key]["text"])/len(data[key]["sentences"])
	# srednia ilosc wyrazow w jednym zdaniu
	item["avgWordsPerSentence"] = len(data[key]["words"])/len(data[key]["sentences"])
	# srednia ilosc interpunkcji na zdanie
	item["avgPunctuationsPerSentence"] = len(data[key]["punctuations"])/len(data[key]["sentences"])
	# uzyte wyrazy
	item["cntWords"] = Counter(data[key]["words"])
	# n-gramy bajtowe
	item["byteNGrams"] = Counter(data[key]["byteNGrams"])
	# n-gramy slowne
	item["wordNGrams"] = Counter(data[key]["wordNGrams"])

	measure[key] = item


import pprint
pp = pprint.PrettyPrinter(indent=4, width=100)
pp.pprint(measure)
