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
  * Czasownik w trzeciej osobie liczby pojedynczej następuje po nazwisku (czasownik w formie męskiej czy tez damskiej)
  * Imiesłowy takie jak 'zamieszkały', 'urodzony'.

Reguły bazujące na innych encjach:

  * Imię poprzedza nazwisko
  * Przezwisko znajduje się na 2 gim miejscu w wyrażeniu trójsłownym (np. Antoni 'Tosiek' Piechnik)
  * Przezwisko znajduje się na 3 cim miejscu w wyrażeniu trójsłownym (np. Antoni Piechnik 'Tosiek')

Reguły bazujące na regułach ortograficznych:

  * Nazwisko zaczyna się dużą literą
  * Nazwisko jest częścią dwu lub trzy wyrazowego wyrażenia w których wszystkie elementy są pisane wielką literą.

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

