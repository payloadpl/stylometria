# Wykorzystanie stylometrii i uczenia maszynowego w informatyce śledczej

Repozytorium zawiera ręcznie odtworzone fragmenty kodu, który niestety jest dostępny tylko w postaci filmu:

https://www.youtube.com/watch?v=Iu-HLy9hICg

https://www.youtube.com/watch?v=rGv4wRE__78

Zobacz też nasze artykuły nt. stylometrii:

https://payload.pl/stylometria/

https://payload.pl/stylometria-policja/


## Instalacja zależności na Linuksie

`apt-get install python3 unrtf catdoc poppler-utils timelimit`

`pip3 install prettyprint matplotlib numpy seaborn`


## Jak to właściwie działa?

1. Klonujemy to repozytorium i tworzymy w nim katalogi:

`mkdir -p Data Process`

2. Do katalogu Data wrzucamy pliki z tekstami do porównania. Obsługiwane są: surowy tekst, Word/Excel do wersji 2003, RTF i PDF. W systemie Linux upewniamy się, że wszystkie pliki mają rozszerenia pisane małymi literami.

3. Sprawdzamy, czy ilość rozpoznanych plików zgadza się z tym, co wrzuciliśmy - jeśli nie, poprawiamy rozszerzenia:

`python3 1_3.py`

4. Przerabiamy pliki w formatach binarnych na format tekstowy:

`python3 2_1_linux.py`

aby to polecenie zadziałało, najpierw zainstaluj zależności (patrz niżej).

5. Wykonujemy kolejno te 2 skrypty - przerabiają one pliki źródłowe z katalogu Data na pliki znormalizowane na potrzeby dalszej obróbki:

`python3 2_2.py`
`python3 2_3.py`

6. Skryptem `3_4_poprawiony.py` uruchamiamy właściwą analizę danych. Na początku tego skryptu znajduje się kilka zmiennych, których tuning może być niezbędny w zależności od analizowanych tekstów.

`python3 3_4_poprawiony.py`

Skrypt tworzy 2 pliki wynikowe: html z tabelką właściwości tekstów, oraz z obrazkiem heatmapy.



# Jak można nam pomóc?

Posiadasz jakieś informacje nt. metod nowszych niż pokazane na tej prezentacji? Albo generalnie jakiekolwiek informacje, które wg Ciebie mogą zainteresować czytelników Payload.pl?

Napisz do nas na kontakt@payload.pl.

Masz wiedzę o nieprawidłowościach u Twojego pracodawcy albo w dowolnej firmie lub instytucji państwowej, urzędzie, czy nawet służbach mundurowych lub specjalnych, ale nie możesz się z taką wiedzą ujawnić ze względu na umowy NDA, złożoną przysięgę czy innego rodzaju zobowiązania?

Jako oficjalnie działający magazyn prasowy, możemy Ci zaproponować ochronę na mocy art. 15 ust. 2 Prawa prasowego (*Dziennikarz ma obowiązek zachowania w tajemnicy danych umożliwiających identyfikację autora materiału prasowego, listu do redakcji lub innego materiału o tym charakterze, jak również innych osób udzielających informacji opublikowanych albo przekazanych do opublikowania, jeżeli osoby te zastrzegły nieujawnianie powyższych danych.*), z zastrzeżeniem art. 16 ust. 1 (*w razie gdy informacja, materiał prasowy, list do redakcji lub inny materiał o tym charakterze dotyczy przestępstwa określonego w art. 240 § 1 Kodeksu karnego*).

# O nas

PAYLOAD - magazyn o ofensywnym bezpieczeństwie IT

https://payload.pl/o-nas/

https://payload.pl/kontakt/
