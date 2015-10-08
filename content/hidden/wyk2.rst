Zajęcia 2: Wykład (SQL cz. 2)
=============================


:date: 2015-10-04
:tags: zaj1, wykład, materiały
:category: materiały
:status: draft

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

Powiedzmy, że mamy w bazie danych tabelę ``student``, która zawiera syntetyczny
klucz główny w kolumnie ``id``. Chcemy do tej bazy danych dodać informację o
ocenach studentów.

Tabela student wygląda tak:

======== ==============
   **student**
-----------------------
   id      name
======== ==============
   1      Jan Kowalski
   2      Józef Nowak
   3      Karol Alfons
======== ==============

Pierwszy pomysł jest taki, stwóżmy tabelę ``OCENA`` która wygląda tak:

======== ============== ===========
     **OCENA**
-----------------------------------
   id     student_id     mark
======== ============== ===========
   1      1               2
   2      1               3
   3      2               4
======== ============== ===========

Kolumna ``student_id`` oznacza identyfikator studenta, który otrzymał daną
ocenę, relatywnie łatwo jest budować zapytania do takiego schematu
(o tym jak się to robi powiem później).

Zasadniczo jest jeden problem z takim schematem, co się stanie jeśli ktoś wprowadzi
do kolumny ``student_id`` wartość np. 500 (której nie ma w kolumnie ``id``
tabeli ``student``)? Jeśli pojawi się taka wartość wiele zapytań nie będzie
działać poprawnie.

By zapobiec temu problemowi można wprowadzić do bazy danych ograniczenie
zwane ``kluczem obcym``, ograniczenie to gwarantuje że jeśli w kolumnie
``student_id`` jest wartość X to istnieje wiersz w tabeli ``student`` o
``id`` równym X.

Klucz obcy robi dwie rzeczy:

* Nie uda się umieścić w tabeli ``OCENA`` wiersza o ``student_id`` łamiącym
  ograniczenie.
* Przy usuwaniu/zmianie wierszy z tabeli ``student`` domyślnie baza danych usunie
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
   **student**
-----------------------
   id      name
======== ==============
   1      Jan Kowalski
   2      Józef Nowak
   3      Karol Alfons
======== ==============

Tabela kurs wygląda tak:

======== ==========================
   **course**
-----------------------------------
   id      name
======== ==========================
   1      Programowanie
   2      Fizyka
   3      Underwater basket weaving
======== ==========================

By zaimplementować relację wiele-do-wielu między tymi tabelami, musimy stworzyć
nową tabelę ``student_course``, tabela ta będzie miała klucze obce, zarówno
do tabeli ``course`` jak i do tabeli ``student``.

============ ======================
  **student_course**
-----------------------------------
student_id   course_id
============ ======================
1            1
1            2
1            3
2            3
============ ======================

Student o ``id`` 1 uczestniczy w kursie o id ``2`` jeśli w tabeli
``student_course`` jest wiersz o wartości ``student_id`` równej 1 oraz
``course_id`` równej 2.

.. note::

  Kolumna ``student_id`` jest kluczem obcym to tabeli ``student``,
  a kolumna ``course_id`` kluczem obcym to tabeli ``course``.

  Dodatkowo


Indeksy
-------

Rozważmy tabelę:

Tabela student wygląda tak:

======== ==============
   **student**
-----------------------
   id      name
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

.. warning::

  Indeksy nie są za darmo, jeśli mamy tabelę z kolumnami ``a``, ``b`` i ``c``,
  to bez indeksów:

  * Przeszukanie (np. za pomocą ``SELECt * FROM T WHERE a=3``) tabeli, będzie
    wymagało odczytania całej tabeli, więc ma zlożoność ``O(n)``.
  * Dodanie wiersza do tabeli zajmie zawsze tyle samo czasu ``O(1)``.

  Jeśli dodamy indeks na kolumnie ``a``, to:

  * Przeszukanie zajmie nam ``O(log(n))``.
  * Dodanie wiersza zajmie również ``O(log(n))``.


Jeśli w tabeli ``T`` kolumna ``id`` jest kluczem głownym baza danych Posgresql
tworzy na niej indeks automatycznie.

Wybieranie daych o relacjach
----------------------------

Aliasy
******

Przy wybieraniu danych z tabeli możemy nadać tabeli alias, tj zamiast napisać:

.. code-block:: sql

  SELECT id from student;

możemy napisać:

.. code-block:: sql

  SELECT s.id FROm student AS s;

Sformuowanie ``student AS s`` oznacza, że w dalszej części zapytania do tabelki
``student`` można odwoływać się poprzez alias ``s``, a wyrażenie ``s.id``
oznacza kolumnę ``id`` z tabeli student.

Wybieranie danych z wielu tabel
*******************************

Gdy na liście ``FROM`` zapytania jest wiele tabel powoduje to wybranie danych
z **kartezjańskiego produktu** wierszy tych tabel.

Jeśli mam tabele:

======== ==============
   **student**
-----------------------
   id      name
======== ==============
   1      Jan Kowalski
   2      Józef Nowak
   3      Karol Alfons
======== ==============

oraz:

======== ==========================
   **course**
-----------------------------------
   id      name
======== ==========================
   1      Programowanie
   2      Fizyka
   3      Underwater basket weaving
======== ==========================

Zapytanie:

.. code-block:: sql

  SELECT s.id, c.id from student AS s, course AS c;

zwróci taki zestaw danych:

======== ==========================

 s.id      c.id
======== ==========================
   1      1
   2      1
   3      1
   1      2
   2      2
   3      2
   1      3
   2      3
   3      3
======== ==========================


.. note::

  Oczywiście dla dużych tabel nikt nie wybiera takiego kartezjańskiego produktu,
  ale bardzo łatwo jest z takiego zestawu za pomocą odpowiedniej klauzuli
  ``WHERE`` wybrać np. kursy danego studenta.

By wybrać informację o średniej dla każdego studenta możemy wykonać takie
zapytanie:

.. code-block:: sql

  SELECT s.id, AVG(m.mark)
    FROM
      student as s,
      mark as m
    WHERE s.id = m.student_id
    GROUP BY s.id
    ORDER BY s.id;

W zapytaniu tym:

* Wybieramy dane z dwóch tabeli ``student`` oraz ``mark``, dodatkowo dodajemy
  do tych tabeli aliasy.
* Za pomocą klauzuli WHERE do wybieramy tylko oceny dla danego studenta.
* Wybieramy średnią ocenę dla każdego studenta.

Wybieranie danych za pomocą operatora ``JOIN``
**********************************************

Bardzo podobne efekty można uzyskać za pomocą operatora ``JOIN``, poniższy
przykład będzie dawał dokładnie te same wyniki co poprzedni:

.. code-block::

  SELECT s.id, AVG(m.mark)
    FROM
      student as s
    JOIN mark as m ON s.id = m.student_id
    GROUP BY s.id
    ORDER BY s.id;

Rozważmy jeszcze jeden problem: powiedzmy że chcemy wypisać listę studentów,
oraz ich średnią, *ale część studentów nie posiada jeszcze żadnych ocen*
w takim wypadku powyższe zapytanie ich pominie, co w naszym przypadku jest
niepożądane.

Rodzaje JOINÓW
**************

W postgresql jest kilka rodzajów ``JOIN``ów:

* Zwykły join ``INNER JOIN``, ``CROSS JOIN``, ``JOIN``, jest równoważny wyrażeniu
  ``FROM table1, table2``, wybiera kartezjański produkt wierszy z obydwu tabel
  ograniczony pewnymi warunkami.
* ``LEFT OUTER JOIN`` podobnie jak join samo jak ``JOIN``, ale gwarantuje że
  w wyniku zapytania będzie obecny każdy wiersz z tabeli
  *po lewej stronie operatora JOIN*

  Implementacja ``LEFT OUTER JOIN`` działa następująco: jeśli jakiś wiersz
  z lewej tabeli byłby usunięty z tego powodu, że nie ma odpowiadających
  mu wierszy tabeli z prawej strony, to i tak jest dodawany do zbioru wynikowego,
  ale przypisuje zakładamy że wszystkie kolumny tabeli z prawej strony przypisane
  do tego wiersza będą miały wartość ``NULL``.

  .. note::

    W zapytaniu:

    .. code-block::

      SELECT s.id, AVG(m.mark)
        FROM student as s LEFT OUTER JOIN mark as m ON s.id = m.student_id
        GROUP BY s.id
        ORDER BY s.id;

    tabelą "po lewej stronie operatora join" jest tabela ``student``.

* ``RIGHT OUTER JOIN`` działa tak samo jak ``LEFT OUTER JOIN``, ale dla tabeli
  *po prawej stronie operatora join*.
* ``OUTER JOIN`` działą tak samo jak ``LEFT OUTER JOIN``, ale dla obydwu tabel.

By wyświetlić również wiersze dla studentów bez ocen, należy zatem wykonać
zapytanie:

.. code-block::

  SELECT s.id, AVG(m.mark)
    FROM student as s LEFT OUTER JOIN mark as m ON s.id = m.student_id
    GROUP BY s.id
    ORDER BY s.id;

Tworzenie schematu bazy danych (opcjonalne)
-------------------------------------------

Pojęcie bazy danych
*******************

System zarządzania bazami danych Postgresql, pozwala na jednym komputerze
zarządzać wieloma bazami danych, do tworzenia baz danych można użyć
programu ``pgadminIII``, albo polecenia
`CREATE DATABASE <http://www.postgresql.org/docs/9.4/static/sql-createdatabase.html>`__.

Bazy danych są od siebie całkowicie odseparowane, "nie widzą" swoich tabel itp.

Dobrą praktyką jest trzymanie oddzielnych projektów (u nas: każdych zajęć) w
oddzielnej bazie danych.

Użytkownicy w bazie dancyh postgresql
*************************************

Domyślnie w bazie danych postgresql zainstalowany jest jeden użytkownik
super-administrator o nazwie ``postgres``.

By stworzyć nowego użytkownika należy wykonać polecenie:
`CREATE USER <http://www.postgresql.org/docs/9.4/static/sql-createuser.html>`__,
lub za pomocą ``pgAdminIII``

.. note::

  Na Windowsie użytkownikowi należy podać hasło, na Linuksie można skorzystać
  z ``peer authentication``, w której użytkownik zalogowany w systemie operacyjnym
  jako użytkownik ``foo`` zostanie zalogowany jako użykownik ``foo`` w bazie
  danycy (jeśli użytkownik o takiej nazwie w bazie danych istnieje).



