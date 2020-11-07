# Niniejszy skrypt jest ręcznie odtworzoną i potem poprawioną wersją tego, co przedstawia film:
# https://www.youtube.com/watch?v=Iu-HLy9hICg



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
		return 0
	return num/denom

# tej funkcji w oryginalnej prezentacji w ogóle nie było - ktoś najprawdopodobniej upraszczał
# na szybko kod i zapomniał o niej - odtworzyliśmy ją dla Was, ale nie mamy pewności, czy poprawnie
# różnica pomiędzy tą funkcją a poprzednią to znak | zamiast & w pierwszej linii kodu
def CosineSimUnion(x, y):
	keys = set(x.keys()) | set(y.keys())

	num = sum([x[k] * y[k] for k in keys])
	sum1 = sum([x[k]**2 for k in keys])
	sum2 = sum([y[k]**2 for k in keys])
	denom = math.sqrt(sum1*sum2)

	if not denom:
		return 0
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
		stat["length"] = len(text)

		# podzial na zdania
		item["sentences"] = GetSentences(text)
		stat["sentences"] = len(item["sentences"])

		# podzial na wyrazy
		item["words"] = GetWords(text)
		stat["words"] = len(item["words"])

		# użyte wyrazy (tablica liczników takich samych wyrazów)
		item["cntWords"] = Counter(item["words"])
		stat["cntWords"] = item["cntWords"].most_common(4)

		# wszystkie uzyte znaki interpunkcyjne
		item["punctuations"] = GetPunctuations(text)
		stat["punctuations"] = len(item["punctuations"])

		# bajtowe n-gramy
		item["byteNGrams"] = GetByteNGrams(text, byteNGram)
		item["cntByteNGrams"] = Counter(item["byteNGrams"])
		stat["cntByteNGrams"] = item["cntByteNGrams"].most_common(4)

		# słowne n-gramy
		item["wordNGrams"] = GetWordNGram(item["words"], wordNGram)
		item["cntWordNGrams"] = Counter(item["wordNGrams"])
		stat["cntWordNGrams"] = item["cntWordNGrams"].most_common(3)

		# średnia długość zdania
		item["avgSentenceLength"] = len(text) / len(item["sentences"])
		stat["avgSentenceLength"] = round(item["avgSentenceLength"], 3)

		# średnia ilość wyrazów w jednym zdaniu
		item["avgWordsPerSentence"] = len(item["words"]) / len(item["sentences"])
		stat["avgWordsPerSentence"] = round(item["avgWordsPerSentence"], 3)

		# średnia ilość interpunkcji na zdanie
		item["avgPunctuationsPerSentence"] = len(item["punctuations"]) / len(item["sentences"])
		stat["avgPunctuationsPerSentence"] = round(item["avgPunctuationsPerSentence"], 3)

		data[fileName] = item
		html[fileName] = stat


# liczymy różne podobieństwa

anonim = data[klucz+".txt"]
sim = {}
for key in data:
	item = {}
	item["długość zdania"] = ValSim(anonim["avgSentenceLength"], data[key]["avgSentenceLength"])
	item["słowa w zdaniu"] = ValSim(anonim["avgWordsPerSentence"], data[key]["avgWordsPerSentence"])
	item["interpunkcja w zdaniu"] = ValSim(anonim["avgPunctuationsPerSentence"], data[key]["avgPunctuationsPerSentence"])
	item["słowa"] = JaccardSim(anonim["cntWords"].keys(), data[key]["cntWords"].keys())
	item["n-gramy słowne (przekrój)"] = CosineSimIntersection(anonim["cntWordNGrams"], data[key]["cntWordNGrams"])
	item["n-gramy bajtowe (przekrój)"] = CosineSimIntersection(anonim["cntByteNGrams"], data[key]["cntByteNGrams"])
	item["n-gramy bajtowe (suma)"] = CosineSimUnion(anonim["cntByteNGrams"], data[key]["cntByteNGrams"])
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

ht = pd.DataFrame.from_dict(html)
text = pd.DataFrame.to_html(ht.transpose()).replace("), (", "<br>").replace("[(", "").replace(")]", "")
with open('wyniki'+fileParams+'.html', 'w', encoding='UTF-8') as dstFile:
	dstFile.write(text)
