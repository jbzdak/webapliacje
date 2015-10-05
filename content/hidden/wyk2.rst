Zajęcia 2: Wykład (SQL cz. 2)
=============================


:date: 2015-10-04
:tags: zaj1, wykład, materiały
:category: materiały

Relacje w relacyjnej bazie danych
---------------------------------

Na razie w tabeli SQL przechowywaliśmy bardzo proste dane, wszystkie dane były
przechowywane w jednej tabeli do której odnosiły się zapytania. Schemat taki
jest bardzo prosty i nie wykorzystuje w pełni możliwości baz relacyjnych,
by je wykorzystać musimy móc wyrazić relacje pomiędzy tabelami.

W bazie danych możliwe są dwa podstrawowe rodzaje relacji:

* Relacje jeden-do-wielu
* Relacje wiele-do-wielu

By zrozumieć jak są one zaimplementowane musimy przypomnieć sobie pojęcie
*klucza głównego* i *klucza obcego*.

klucz główny *z ang.* primary key

  To kolumna (lub zestaw kolumn) która jednoznacznie identyfikuje dany wiersz,
  spełnia ona dwa wymagania:

  * Wartości w tej kolumnie są unikalne dla każdego wiersza.
  * Wartości w tej kolumnie nigdy nie przyjmuje wartości ``NULL``.

By jednoznacznie zidentyfikować wiersz w tabeli, starczy znać wartość jego klucza
głownego.

Relacja jeden-do-wielu
----------------------

Powiedzmy, że mamy w bazie danych tabelę ``STUDENT``, która zawiera syntetyczny
klucz główny w kolumnie ``id``. Chcemy do tej bazy danych dodać informację o
ocenach studentów.

Tabela student wygląda tak:

======== ==============
   **STUDENT**
-----------------------
   id      Nazwa
======== ==============
   1      Jan Kowalski
   2      Józef Nowak
   3      Karol Alfons
======== ==============

Pierwszy pomysł jest taki, stwóżmy tabelę ``OCENA`` która wygląda tak:

======== ============== ===========
     **OCENA**
-----------------------------------
   id     id_studenta   Ocena
======== ============== ===========
   1      1               2
   2      1               3
   3      2               4
======== ============== ===========

Kolumna ``id_studenta`` oznacza identyfikator studenta, który otrzymał daną
ocenę, relatywnie łatwo jest budować zapytania do takiego schematu
(o tym jak się to robi powiem później).

Zasadniczo jest jeden problem z takim schematem, co się stanie jeśli ktoś wprowadzi
do kolumny ``id_studenta`` wartość np. 500 (której nie ma w kolumnie ``id``
tabeli ``STUDENT``)? Jeśli pojawi się taka wartość wiele zapytań nie będzie
działać poprawnie.

By zapobiec temu problemowi można wprowadzić do bazy danych ograniczenie
zwane ``kluczem obcym``, ograniczenie to gwarantuje że jeśli w kolumnie
``id_studenta`` jest wartość X to istnieje wiersz w tabeli ``STUDENT`` o
``id`` równym X.

Klucz obcy robi dwie rzeczy:

* Nie uda się umieścić w tabeli ``OCENA`` wiersza o ``id_studenta`` łamiącym
  ograniczenie.
* Przy usuwaniu/zmianie wierszy z tabeli ``STUDENT`` domyślnie baza danych usunie
  wszystkie odpowiadające danemu studentowi oceny (zachowanie to jest
  konfigurowalne).

.. note::

  Uwaga: poprawna implementacja klucza obcego, działająca w przypadku
  równoległej edycji tabeli przez wielu użytkowników jest **nietrywialna**.


.. note::

  Naturalny klucz główny (*z ang.* natural key), to klucz główny, na
  który składają się kolumny już istniejące w bazie danych mające
  znaczenie w *świecie rzeczywistym*.

  Przykładowo w tabeli przechowującej
  studentów możemy uznać, że dobrym kluczem głównym będzie unikalny numer PESEL.

  Syntetyczny klucz główny (*z ang.* synthetic key), to klucz głowny, którego
  wartość ma znaczenie tylko wewnątrz bazy danych, i została przez nią
  przypisana. Praktycznie zawsze syntentyczne klucze głowne generuje się za
  pomocą "sekwencji", tj. są one przyznawane "po kolei".

  Przykładowo uczelnia przyznaje studentom syntetyczne identyfikatory (nr. indeksu).

  Według wielu administratorów w zasadzie zawsze należy dodawać
  do tabeli klucz syntetyczny. Ma on takie zalety:

  * Jego wartość nigdy się nie zmienia (zmianę wartości w klucza naturalnego
    może wymusić zmiana w świecie).
  * Nie zależy od zachowania świata zewnętrznego.
  * Klucze sztuczne są mniejsze, generalnie są przechowywane jako 8 (czasem 16)
    bitowy typ stałoprzecinkowy (potocznie: ``long`` lub ``long long``).
  * Joiny po kluczach sztucznych mogą być szybsze (sztuczne klucze główne
    są mniejsze)

  Przy naturalnych kluczach głównych łatwo jest przapić nieoczywiste relacje w
  świecie rzeczywistym, które "psują" założenia (np. student z Ukrainy nie musi
  mieć przyznanego numeru pesel).


Relacja wiele-do-wielu
----------------------

Powiedzmy że do naszego schematu chcemy dodać informację o tym na jakie przedmioty
student się zapisał. Jeden student może zapisać się na wiele przemdiotów, no i
oczywiście w jednym przedmiocie bierze udział wielu studentów. Takiej
relacji nie da się zaimplementować za pomocą pojedyńczego klucza obcego.

Tabela student wygląda tak:

======== ==============
   **STUDENT**
-----------------------
   id      Nazwa
======== ==============
   1      Jan Kowalski
   2      Józef Nowak
   3      Karol Alfons
======== ==============

Tabela kurs wygląda tak:

======== ==========================
   **KURS**
-----------------------------------
   id      Nazwa
======== ==========================
   1      Programowanie
   2      Fizyka
   3      Underwater basket weaving
======== ==========================

By zaimplementować relację wiele-do-wielu między tymi tabelami, musimy stworzyć
nową tabelę ``UCZESTNICY_KURSOW``, tabela ta będzie miała klucze obce, zarówno
do tabeli ``KURS`` jak i do tabeli ``STUDENT``.

============ ======================
  **UCZESTNICY_KURSOW**
-----------------------------------
id_studenta  id_kursu
============ ======================
1            1
1            2
1            3
2            3
============ ======================

Student o ``id`` 1 uczestniczy w kursie o id ``2`` jeśli w tabeli
``UCZESTNICY_KURSOW`` jest wiersz o wartości ``id_studenta`` równej 1 oraz
``id_kursu`` równej 2.

.. note::

  Kolumna ``id_studenta`` jest kluczem obcym to tabeli ``STUDENT``,
  a kolumna ``id_kursu`` kluczem obcym to tabeli ``KURS``.

  Dodatkowo


Indeksy
-------

Rozważmy tabelę:

Tabela student wygląda tak:

======== ==============
   **STUDENT**
-----------------------
   id      Nazwa
======== ==============
   15     Jan Kowal
   1      Jan Kowalski
   10     Józef Nowak
   ...     ...
 500000   Karol Alfons
======== ==============

Dane nieposortowane
*******************

Naszym zadaniem jest znaleźć imie i nazwisko studenta o ``id`` równym 234,
ile czasu zajmie nam (średnio) znalezienie tego studenta w funkcji ilości
rekordów w bazie danych?

W tak postawionym problemie średnio należy sprawdzić :math:`\frac{N}/{2}`
rekordów zanim znajdziemy ten o odpowiednim ID.

Dane posortowane
****************

Ile czasu zajmie odnalezienie studenta jeśli dane w tabeli są posortowane
względem indeksu? W tym przypadku będzie trzeba sprawdzić :math:`\log_2 N`
rekordów.

.. note::

  Można do tego wykorzystać algorytm zwany `binarnym przeszukiwaniem
  <https://en.wikipedia.org/w/index.php?title=Binary_search_algorithm&oldid=683589688>`__.

  Algorytm ten opiera się na następującej obserwacji, weźmy element E
  znajdujący się w środku tabeli, jego ``id`` może być:

  * Równe poszukiwanemu --- wtedy problem jest rozwiązany
  * Mniejsze od poszukiwanego --- wtedy wszystkie elemementy znajdujące się
    przed E również mają ``id`` mniejsze od poszukiwanego więc można je
    wykluczuć.
  * Większe od poszukiwanego --- wtedy wszystkie elemementy znajdujące się
    za E również mają ``id`` większe od poszukiwanego więc można je
    wykluczuć.

Indeksy
*******

Przechowywanie posortowanych danych w bazie jest niepraktyczne, główne powody
to:

* Konieczność utrzymywania kilku uporządkowań na raz. Chcielibyśmy zarówno móc
  szybko wyszukiwać studenta znając jego ``id``, numer pesel jak i imię.
* Koszt utrzymania sortowania jest duży --- jeśli okaże się że nowy element
  trzeba wstawić na początku tabeli wszystkie kolejne elementy trzeba przesunąć.

Użyto więc innego rozwiązania: do kolumny można dodać indeks, indeks pozwala
szybciej wyszukiwać dane w tabeli jeśli przeszukujemy tabelę z użyciem
zindeksowanych kolumn. Istnienie indeksów spowalnia proces dodawania danych
do tabeli.

.. note::

  Istnieje dużo typów indeksów, i każdy typ ma inne zastosowanie, detale jednak
  przekraczają zakres tego przedmiotu.

  Istnieją też indeksy obejmujące wiele kolumn.

Jeśli w tabeli ``T`` kolumna ``id`` jest kluczem głownym baza danych Posgresql
tworzy na niej indeks automatycznie.




Tworzenie schematu bazy danych (opcjonalne)
-------------------------------------------
