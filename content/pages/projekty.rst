Projekty
========

:date: 2014-09-16
:category: highlighted


Projekty generalnie mają raczej mieć charakter utylitarny, czyli powinno to być:

1. Projekt który i tak musicie napisać.
2. Projekt który napisaiście w C i chcecie spróbować zrobić go w Pythonie.


Przykłady projektów
-------------------

Oczywiście można zrobić przykładowy projekt, jednak zasadniczo mają one
ustawiać poziom projektów.

Projekt wikipedia
*****************

Program wyciąga n-gramy z wikipedii i na ich podstawie generuje sugester który
potrafi uzupełniać kolejne litery słowa.

Nie jest to do końca program z trzecich zajęć, są takie dodatkowe wymagania:

1. Dostarczacie Państwo cały produkt, polecenie generujące n-gramy i sugester.
2. Program powinien działać **szybko** może jakieś wstawki w C? Może zamiast
   trzymać wszystko w słowniku trzeba część danych trzymać na sortowanej liście.
   Może możemy darować sobie n-gramy które mają częstotliwość mniejszą niż jeden
   na milion?

   Liczę na inwencję ale zawsze będę służyć radą.
3. Podczas generowania bazy n-gramów program musi pracować równolegle
   na przynajmniej dwóch rdzeniach.
4. Maksymalne zużycie pamięci RAM: 750MB na rdzeń.
5. Mile widziane użycie porządnego parsera wikitekstu.


