Wstęp
=====

Projekt został zrealizowany w ramach przedmiotu Inżynieria Oprogramowania.
Głównym zadaniem projektu jest utworzenie systemu typu Named Entity
Recognition - wyszukiwanie konkretnego typu słów w tekście stron WWW (takich
jak nazwiska, imiona, czy pseudonimy).  

Projekt docelowo ma być integralną częścią systemu SWAT. Sercem systemu jest
algorytm łączący zestawy reguł językowych do utworzenia optymalnych kombinacji
rozpoznających encje danego typu w tekście. Dzięki takiemu podejściu nie tylko
wykorzystuje podane reguły do stworzenia mozliwie najlepszej kombinacji, ale
również pozwoli na łatwe dodanie nowych reguł do aplikacji.

Struktura systemu
=================

System składa się z następujących części:

Tagger tekstów do testów
------------------------

Skrypt mający na celu skanowanie przykładowych tekstów a następnie generowania
specyficznych raportów odnośnie ilości wystąpień poszczególnych encji w tekście.

Dzięki skryptowi będzie możliwe przygotowanie tekstów odpornych na konkretne
reguły, oraz zwiększenie możliwości testowania aplikacji.  Tagger bazować
będzie na liście danych encji (np. bazie nazwisk), z której nie będziemy
korzystać w pracy Rdzenia aplikacji.

Generator reguł n-gramowych
---------------------------

W związku z chęcią implementacji reguł bazujących na najpopularniejszych
n-gramach utworzony został generator reguł który zbiera najczęściej występujące
n {3,4,5} gramy występujące w tekstach przed nazwiskami oraz po, które posłużą
za wykładnię do łączenia reguł.  Do tworzenia list n-gramów potrzebny jest
odpowiedni korpus zawierający nazwiska, jak i również ich baza, dzięki której
można je wykrywać w tekście.  Generator, w celu uniknięcia zbierania nic nie
znaczących n-gramów porównywał będzie nie tylko jego zawartość ale również
pozycję w słowie.

Rdzeń 
----- 

W tej części aplikacji znajduje się zaimplementowany algorytm który
aplikuje przygotowane i wygenerowane reguły do wyszukiwania nazwisk w tekście.
Przygotowanych została konkretna liczba reguł, oraz ich przykładowe kombinacje
dzięki którym będzie można porównywać ich efektywność na tekstach przykładowych.
Rdzeń pobiera również odpowiednie listy n-gramów o różnej długości, wygenerowane
uprzednio przez Generatora reguł n-gramowych.  Rdzeń został napisany w języku
Python, dzięki czemu wyjątkowo proste jest ewentualne dodanie dodatkowych reguł.

Opis działania aplikacji
========================

Zastosowane reguły (przykłady)
------------------------------

Reguły kontekstowe:

  * Słowo 'doktor' poprzedza nazwisko
  * Słowo 'mgr' poprzedza nazwisko
  * Słowo 'mgr inż.' poprzedza nazwisko
  * Reszta tytułów naukowych.
  * Słowo 'lek.'
  * Słowo 'mec.'
  * Słowo 'arch.'
  * Reszta tytułów zawodowych.
  * Słowo 'pan' poprzedza nazwisko
  * Słowo 'pani' poprzedza nazwisko
  * Czasownik w trzeciej osobie liczby pojedynczej następuje po nazwisku
    (czasownik w formie męskiej czy tez damskiej)
  * Imiesłowy takie jak 'zamieszkały', 'urodzony'.

Reguły bazujące na innych encjach:

  * Imię poprzedza nazwisko
  * Przezwisko znajduje się na 2 gim miejscu w wyrażeniu trójsłownym (np. Antoni
    'Tosiek' Piechnik)
  * Przezwisko znajduje się na 3 cim miejscu w wyrażeniu trójsłownym (np. Antoni
    Piechnik 'Tosiek')

Reguły bazujące na regułach ortograficznych:

  * Nazwisko zaczyna się dużą literą
  * Nazwisko jest częścią dwu lub trzy wyrazowego wyrażenia w których wszystkie
    elementy są pisane wielką literą.

Reguły n-gramowe:

  * Nazwisko kończy się charakterystycznym sufiksem (np. '-ski', '-icz')
  * Pozostałe reguły generowane poprzez system


Dzięki zastosowaniu systemu reguł oraz ich kombinacji, bez problemu będzie można
do systemu wstawiać dodatkowe reguły co usprawni jego prace oraz uświetni wyniki
osiągane przez algorytm. 

Wielką zaletą zastosowanego algorytmu jest fakt, iż reguły tak naprawdę nie
muszą dokładnie precyzować wystąpień danych encji (tu nazwisk), ale jedynie
sprzyjające temu warunki (które w połączeniu z innymi warunkami mogą definiować
reguły).


Zastosowane technologie
=======================

Do implementacji znacznej części aplikacji wykorzystano język Python, ze względu
na jego perfekcyjne przystosowanie do prac nad przetwarzaniem języka
naturalnego.

W związku z faktem, iż projekt SWAT jest napisany w języku Java, należało
wykorzystać swojego rodzaju pomost pomiędzy naszą częścią aplikacji a
dotychczasowymi interfejsami wyszukiwania encji w tekstach. W tym celu
wykorzystano Jythona, czyli implementację języka Python napisaną w języku
Java.

Poza Jythonem korzystano z funkcji wbudowanych w język Python, związanych z
przetwarzaniem tekstu oraz konwersją między różnego rodzaju kodowaniem
(pozwalająca na komunikację oraz transfer danych z poziomu Javy do Pythona i na
odwrót).

Opis zastosowanych narzędzi
===========================

Jython
------

Implementacja języka Python w Javie pozwalający na
transparentna komunikacje miedzy Pythonem a klasami Javy. Okazał się
niezastąpiony przy wiązaniu aplikacji Rdzenia z dotychczasowymi interfejsami
projektu SWAT. 

Dzięki wykorzystaniu zewnętrznych bibliotek związanych m.in. z kodowaniem udało
się bez najmniejszych problemów wywoływać klasy napisane w Rdzeniu (w Pythonie)
z poziomu Javy, jak również importować wszelakie pakiety projektu SWAT do kodu
aplikacji w Pythonie.

Wiecej informacji na stronie Jythona: http://www.jython.org

encodings
---------

Moduł Pythona zawierający zbiór najważniejszych i
najpopularniejszych kodowań oraz metod z nimi związanych.

Dzięki niemu udało się rozwiązać problem związany z komunikacją (w szczególności
przesyłaniem polskich znaków z obiektów Javy do obiektów Pythona)

egothor
-------

Silnik full-text search z którego korzystano przy
tworzeniu systemu.

Wiecej informacji na stronie: http://www.egothor.org/

Morfologik
----------

Analizator morfologiczny, słownik morfologiczny,
korektor gramatyczny.

Wiecej informacji na stronie: http://morfologik.blogspot.com/


Wyniki
======

Reguły proste
-------------

Zgodnie z oczekiwaniami, wyniki reguł prostych charatkeryzowały się skrajnie
różnymi wartościami współczynników. Albo osiągały wysokie pokrycie kosztem
dokładności (reguła wielkich liter), albo przeciwnie - wysoką dokładność
kosztem pokrycia (poszukiwanie w liście nazwisk). Kompromis pomiędzy tymi
wynikami udało się osiągnąć dzięki zastosowaniu reguł złożonych.

Reguły złożone
--------------

Reguły złożone pomogły zamortyzować wspomniane wyżej różnice. Dzięki złożeniu
reguł w nową, dopasowującą słowo jedynie gdy odpowiednio duża ich część (próg)
to robiła, udało się nieco płynniej kontrolować relację między dokładnością a
pokryciem. Osiągnięto to dzięki odpowiedniemu dopasowywaniu wartości progu.


Podręcznik użytkownika
======================

Korzystanie z klas Jythona w Javie
----------------------------------

Aby móc skorzystać z detektorów zaimplementowanych w Jythonie na poziomie Javy,
należy najpierw je zimportować przy użyciu klasy JythonFactory
`jyinterface.factory`:

.. code-block:: java

	String interfaceName = "org.ppbw.agh.swat.hoover.smith.quantum.detection.IQuantumDetector";
	Object obj = JythonFactory.getJythonObject(interfaceName,
				"pyner/detectors.py", "CapitalDetector");
	IQuantumDetector detector = (IQuantumDetector) obj;

Następnie można korzystać z detektora tak jak z każdej klasy implementującej
interfejs `org.ppbw.agh.swat.hoover.smith.quantum.detection.IQuantumDetector`.

Częścią projektu jest klasa `agh.io.Main` w której zamieszczono przykładowe
użycie detektorów zaimplementowanych w Jythonie.


Implementacja detektorów w Jythonie
-----------------------------------

Detektory w projekcie pyner to proste funkcje o prostym interfejsie (opisanym w
dokumentacji modułu :mod:`pyner.rules`). Zgodnośc z interfejsem 
`org.ppbw.agh.swat.hoover.smith.quantum.detection.IQuantumDetector` uzyskano
generując klasy na podstawie funkcji. Zajmuje się tym funkcja
:func:`pyner.detectors.gen_detector`, która otrzymując obiekt funkcji zwraca obiekt
metaklasy. Przykładowe użycie funkcji gen_detector::

	NgramsNeighboursDetector    = gen_detector(rules.ngrams_neighbours)
	PrefixesDetector            = gen_detector(rules.prefixes)
	SuffixesDetector            = gen_detector(rules.suffixes)
	CorpusDetector              = gen_detector(rules.in_name_corpus)
	CapitalDetector             = gen_detector(rules.starts_with_capital)
