# https://www.youtube.com/watch?v=Iu-HLy9hICg, 24:08
# normalizacja danych - kasujemy dziwne znaki

import string
import re
import os

goodCharacters = string.ascii_letters + string.punctuation + string.digits + 'ąćęłńóśżź' + 'ąćęłńóśżź'.upper() + '\s'

dir = os.getcwd() + "/Process/"
for fileName in os.listdir(dir):

	with open(dir + fileName, 'r', encoding='UTF-8') as srcFile:
		text = srcFile.read()
		text = re.sub(r'[^'+goodCharacters+']', '', text)
		text = re.sub('[\s\t\n]+', ' ', text)

	with open(dir + fileName, 'w', encoding='UTF-8') as dstFile:
		dstFile.write(text)

# od 26:11 prezentujący wspomina o możliwych dodatkowych technikach czyszczenia:
# - usunięcie stopwords, które nic nie wnoszą
# - usunięcie fleksji i pozostawienie tylko rdzenia danego slowa - z tym że ta technika wplynie na działanie kolejnych skryptów


# moim (Tomasz Klim) zdaniem warto tutaj obsłużyć przypadki:
# - skróty z kropkami - "np."
# - liczby z przecinkami i kropkami w treści
