O przedmiocie
=============

:date: 2014-09-30
:slug: o-przedmiocie
:category: highlighted

Grupa docelowa
--------------

Zajęcia przeznaczone są dla studentów posiadających podstawową wiedzę dotyczącą
programowania. Nie zakładam znajomości języka Python, osoby które znają ten
język również znajdą coś dla siebie --- ponieważ koncentrować się będę
na wykorzystaniu konkretnych narzędzi Pythona do rozwiązywania
problemów naukowych.

Na zajęciach nie będzie informacji o tym czym jest zmienna, pętla, funkcja
czy klasa; będzie natomiast powiedziane jak działąją zmienne w Pythonie
(jaki mają zakres), jak definiuje się klasy i funkcje.
Będę starał się też pokazywać jak Python różni się od C++ czy Javy.

Cel przedmiotu
--------------

Co student będzie umiał po zajęciach:

* (O)Programowanie typowych problemow naukowych w języku python
* Praca z medium-scale data (dane mieszczące się w pamięci ram) ~20GB
* Programowanie równoległe na CPU

  * Głównie w przypadkach na których paralelizacja jest trywialna
    (w takim przypadku zadanie da się podzielić na niezależne od siebie
    podzadania)
  * Może zdążymy wyjść poza ten zakres

Co jest poza zakresem:

* Paralelizacja na GPU

  * Polecam wziąć kurs (coursera, edX) z Cudy/OpenCL a potem zaznajomić się z
    PyCuda i PyOpenCL

* Pisanie wydajnych algorytmów pracujących równolegle na jednym zestawie danych
  np. równoległe sortowanie, równoległy skan
* Ogarnianie terabajtowych zestawów danych

  * Ogarnięcie 1000 zestawów danych po 1GB jest w zakresie :)

Sylabus
-------

Zajęcia będą prowadzone pierwszy raz, więc proszę spodziewać się dawki bałaganu.
Nie wiem co dla Państwa będzie proste, więc sylabus jest tylko lekko naszkicowany.

Przedmiot jest w formacie 10 x 3h, co razem daje 30 godzin.

Blok 1: Podstawy Pythona
^^^^^^^^^^^^^^^^^^^^^^^^

Blok ten będzie trwał dwa/trzy zajęcia.

**Cel:** Zaznajomić studentów z językiem Python, oraz pojęciami takimi jak:

* Język dynamiczny
* Duck-typing
* Domknięcie (*z ang.* closure)
* Moduł, paczka Pythona

**Narzędzia:** Studenci będą tworzyć kod w edytorze tekstu i wykonywać za pomoca
interpretera Pythona. Zostaną zapoznani z podstawami systemu kontroli wersji GIT.

**Zadanie na koniec bloku** (do wykonania na zajęciach): napisanie programu
przetwarzającego duży (10GB) plik tekstowy.

Blok 2: ``numpy`` podstawowe narzędzie do analizy dużych zestawów danych
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Blok ten będzie trwał dwa/trzy zajęcia.

**Cel:** Zaznajomić studentów z pracą w bibliotece ``numpy``,
oraz takimi zagadnieniami jak:

* Wektoryzacja
* Układ pamięci (memory layout)
* Tworzenie i format plików binarnych
* Wywołanie systemowe ``mmap`` (i odpowiednik na Windowsie)

**Narzędzia:** Studenci będą pracować w IDE PyCharm. Dodatkowo studenci zapoznają się 
z pojęciem środowiska virtualnego oraz nauczą się instalować Pythonowe moduły
za pomocą managera paczek PIP, oraz narzędzi setuptools.

**Zadanie na konice bloku** (do wykonania na zajęciach): napisanie programu
wydajnie pracującego na dużym zestawie danych binarnych.

Blok 3: Równoległe przetwarzanie danych za pomocą Pythona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Blok ten będzie trwał dwa/trzy zajęcia.


**Cel:** W ramach zajęć studenci zapoznają się problematyką równoległego przetwarzania
dużych zestawów danych. W tym z takimi zagadnieniami jak.

* Różnica między wątkiem a procesem

  * Wielowątkowość a wieloprocesowość 

* Operacja map i map-reduce

  * Wykonywanie wieloprocesowej operacji map

* IPython notebook jako narzędzie do równoległego przetwarzania danych

**Narzędzia:** Studenci będą pracować w programie IPython notebooks.
Tutaj zapoznają się z biblioteką ``pandas``

**Zadanie na konice bloku** (do wykonania na zajęciach): napisanie programu
wydajnie pracującego na dużym zestawie danych binarnych.


Pozostałe zagadnienia
^^^^^^^^^^^^^^^^^^^^^

Pozostałe zagadnienia dobiorę do zainteresowań studentów. mam takie propozycje
(propozycje raczej na pół zajęć/jedne zajęcia każda):

* Integracja Pythona z kodem C/C++/Fortrana

  * Biblioteki Cyhton, ``scipy.weave``

* Zastosowanie Pythona do tworzenia skryptów
* Zastosowanie Pythona jako narzędzia ułatwiającego uruchamianie istniejącego
  kodu symulacyjnego napisanego w mniej przyjaznych językach.
* Przygotowywanie dokumentacji i stronu projektu. Łatwoe tworzenie stron
  (na przykład stron przedmiotów ;)).
* Piękne wykresy za pomocą `matplotlib`

Zgłaszanie zagadnień
--------------------

Zapraszam Państwa do zgłaszania pomysłów na potrzebne Wam tematy zajęć,
najprościej będzie wysłać temat pocztą, jeśli zbierze się więcej tematów
to zrobię głosowanie.



Regulamin oceniania
-------------------

Średnia z przedmiotu jest średnią ważoną następującyh składników:

* Ocena z laboratoriów (waga 2)

  * Każde laboratoria kończą się napisaniem programu, zasadniczo program
    jest możliwy do stworzenia na zajęciach ale możliwe będzie oddanie
    go na konsultacjach bądź następnych zajęciach.

* Ocena z kolokwiów wejściowych (waga 1)

  * Będzie 5-6 kolokwiów wejściowych/zejściowych
  * Poza przypadkiem osób które nie uzyskają 50% ze wszystkich wejściowek
    popraw nie przewiduję.

* Ocena z projektu (waga 1)


Wykonanie projektu nie jest konieczne do zaliczenia (ocena wtedy wynosi 2.0 i
jest wliczania do średniej opisanej powyżej), natomiast konieczne jest
uzyskanie 50% punktów z każdej wejściówki.


Zajęcia
-------

Materiały na zajęcia będą umieszczane na stronie ok. tydzień przed zajęciami
studenci powinni się z nimi zapoznać.

Zajęcia zaczynamy od ok. 45 minut wprowadzenia w formie wykładu. Przez pozostały
czas studenci wykonują zadania oceniane na koniec zajęć.

Studenci na zajęciach pracują w parach, pary będą ustalone na początku zajęć
(jeśli jednak wykryję zespół w którym praca będzie rozłożona nierównomiernie
rezerwuję sobię prawo do rozbicia go).

Ponieważ wymuszenie pracy w parach może być niespotykane, szbkie wyjaśnienie:

* Z mojego doświadczenia wynika że czasem
  studenci mając przed sobą trudne zadanie (u mnie nie ma prostych ;)) zacinają
  się i zaczynają walić głową w ścianę, empirycznie stwierdzam że w zespole
  zjawisko to nie występuje.
* Ponieważ wiele problemów/wątpliwości jest rozwiązywanych wewnątrz zespołu
  mniej mojego czasu jest poświęcanego bieżącemu wspomaganiu studentów i mogę 
  więcej czasu na trudniejsze problemy.
* Jeśli ktoś się nie przygotował na zajęcia, jest szansa że druga osoba go
  wspomoże.

