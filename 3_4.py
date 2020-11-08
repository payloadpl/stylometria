# Niniejszy skrypt jest ręcznie odtworzoną i potem poprawioną wersją tego, co przedstawia film:
# https://www.youtube.com/watch?v=Iu-HLy9hICg

# Niektóre rzeczy zostały odtworzone z głowy - część z nich została potem zweryfikowana w oparciu o drugą
# prezentację: https://www.youtube.com/watch?v=rGv4wRE__78 (np. brakująca w pierwszej funkcja CosineSimUnion),
# inne zaś tylko empirycznie.



# długości n-gramów (nie mają jednej "poprawnej" wartości, raczej trzeba je dobierać eksperymentalnie do specyfiki portównywanych tekstów)
wordNGram = 3
byteNGram = 4

# nazwa pliku (bez rozszerzenia .txt), który będzie wzorem, do którego będzie porównywana reszta
klucz = "misja"



import math
import os
import re
import string
from collections import Counter

def ValSim(x, y):
	return (2*x*y)/(x**2+y**2)

def CosineSimIntersection(x, y):
	keys = set(x.keys()) & set(y.keys())

	num = sum([x[k] * y[k] for k in keys])
	sum1 = sum([x[k]**2 for k in keys])
	sum2 = sum([y[k]**2 for k in keys])
	denom = math.sqrt(sum1*sum2)

	if not denom:
		return 0.0
	return num/denom

def CosineSimUnion(x, y):
	keys = set(x.keys()) | set(y.keys())

	num = sum([x[k] * y[k] for k in keys])
	sum1 = sum([x[k]**2 for k in keys])
	sum2 = sum([y[k]**2 for k in keys])
	denom = math.sqrt(sum1*sum2)

	if not denom:
		return 0.0
	return num/denom

def JaccardSim(A, B):
	return len(A&B)/len(A|B)

# do 32:33 prezentujący tłumaczy prawdopodobieństwo Jaccarda (podobieństwo dwóch zbiorów)

# teraz doklejamy to co było stworzone wcześniej

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



dir = os.getcwd() + "/Process/"
data = {}
html = {}

for fileName in os.listdir(dir):
	with open(dir + fileName, 'r', encoding='UTF-8') as srcFile:
		item = {}
		stat = {}
		text = srcFile.read().lower()
		item["text"] = text

		# podzial na zdania
		item["sentences"] = GetSentences(text)
		stat["sentences"] = len(item["sentences"])
		# podzial na wyrazy
		item["words"] = GetWords(text)
		stat["words"] = len(item["words"])
		# wszystkie uzyte znaki interpunkcyjne
		item["punctuations"] = GetPunctuations(text)
		stat["punctuations"] = len(item["punctuations"])
		# bajtowe n-gramy
		item["byteNGrams"] = GetByteNGrams(text, byteNGram)
		# slowne n-gramy
		item["wordNGrams"] = GetWordNGram(item["words"], wordNGram)

		data[fileName] = item
		html[fileName] = stat


import pprint
pp = pprint.PrettyPrinter(indent=4, width=100)
pp.pprint(html)


measure = {}
for key in data:
	item = {}

	# srednia dlugosc zdania
	item["avgSentenceLength"] = len(data[key]["text"])/len(data[key]["sentences"])
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


# liczymy różne podobieństwa

anonim = measure[klucz+".txt"]
sim = {}
for key in measure:
	item = {}
	item["avgSentenceLength"] = ValSim(anonim["avgSentenceLength"], measure[key]["avgSentenceLength"])
	item["avgWordsPerSentence"] = ValSim(anonim["avgWordsPerSentence"], measure[key]["avgWordsPerSentence"])
	item["avgPunctuationsPerSentence"] = ValSim(anonim["avgPunctuationsPerSentence"], measure[key]["avgPunctuationsPerSentence"])
	item["cntWords"] = JaccardSim(anonim["cntWords"].keys(), measure[key]["cntWords"].keys())
	item["wordNGramsIntersection"] = CosineSimIntersection(anonim["wordNGrams"], measure[key]["wordNGrams"])
	item["byteNGramsIntersection"] = CosineSimIntersection(anonim["byteNGrams"], measure[key]["byteNGrams"])
	item["byteNGramsUnion"] = CosineSimUnion(anonim["byteNGrams"], measure[key]["byteNGrams"])
	sim[key] = item

del sim[klucz+".txt"]


import matplotlib
matplotlib.use('Agg')

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

import pandas as pd
df = pd.DataFrame.from_dict(sim)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_values = scaler.fit_transform(df)
df.loc[:,:] = scaled_values

import seaborn as sns
sns.set(rc={'figure.figsize':(10,10)})
ax = sns.heatmap(df.T, annot=True)
fileParams = '-w'+str(wordNGram) + '-b'+str(byteNGram)
fig = ax.get_figure().savefig(klucz+fileParams+'.png', format='png')
