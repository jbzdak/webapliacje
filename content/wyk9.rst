Tranzakcie w bazie danyh
========================

:date: 2015-12-14
:tags: zaj9, wykład, materiały
:category: materiały


.. note::

  Wykład do pobrania również w wersji PDF.

  .. raw:: html

     <a href="downloads/pdfs/wyk9.pdf">Wersja pdf tutaj</a>


Zacznijmy od przykładu, mam system bazodanowy, który implementuje funkcjonalność
przelewów. Algorytm przelewu działa następująco:

1. Sprawdzamy czy istnieje konto A,
2. Sprawczamy czy istnieje konto B,
3. Sprawdzamy czy konto ma saldo pozwalające na przelew,
4. Zmieniamy saldo konta A, zmniejszając je o K (kwotę przelewu),
5. Zmieniamy saldo konta B, zwiększając je o K.

Saldo konta A ma 200 zł, a użytkownik próbuje **na raz** dokonać dwóch przelewów:

1. Z konta A do konta B na kwotę 200 zł,
2. Z konta A do konta C na kwotę 200 zł.

Jaki jest wynik tej operacji:

A. Na koncie A jest -200 zł, a na kontach B i C po 200;
B. Na koncie A jest 0 zł, a na kontach B i C po 200;
C. Na koncie A jest 0 zł, a na kontach B i C po 0;

Odpowiedź brzmi: Nie wiadomo! Ten algorytm zawiera, tzw. *hazard*
(lub *race condition*)! W zależności od czasów uruchomienia tych operacji
możliwe są różne ostateczne wyniki.

ACID
----

ACID to podstawowe założenia systemu tranzakcyjnego:

Atomicity
  Transakcje są atomowe, albo się udają, albo nie, albo wykonują wszystkie zmiany
  w baziedanych, albo żadnej.

  Transakcja, która się powiodła jest zapisywana (z. ang. *commit*), a transakcja
  która się nie powiodła wycofywana (z. ang. *rollback*).

Consistency
  Po zakończeniu każdej transakcji baza danych jest w **spójnym** stanie, tj.
  wszystkie ograniczenia są spełnione.

Isolation
  Transakcje są od siebie odizolowane, tj. nie widzą swoich zmian.

Durability
  Po zakończeniu transakcji dane są zapisane w taki sposób, że nawet serwer
  będzie je pamiętać nawet po **awarii**.

  Czym jest awaria trudno powiedzieć, może to być:

  1. Utrata zasilania.
  2. Utrata części komputerów z klastra.


Bardzo trudno jest osiągnąć którąkolwiek z zasad ACID, bez spełnienia pozostałych.
Jeśli transakcje nie są izolowane, bardzo trudno zachować spójnośc danych,
jeśli nie ma durability, po awarii klastra dane mogą być niespójne itp.


Anomalie
********

Dirty Read
  Jeśli jedna transakcja widzi dane zapisane przez inną, która nie jest
  zakończona mamy doczynienia z anomalią Dirty Read.

  Przykład dlaczego jest groźna:

  1. Transakcja x dodaje do salda konta A 200 zł (konto było puste).
  2. Transakcja y wykonuje przelew z konta A do konta B na kwotę 200zł i
     jest commitowana.
  3. Transakcja x jest rollbackowana.

Non-Repeatable Read
  Jeśli jedna transakcja zmienione wartości wierszy zapisane przez inną, która
  się zakończyła.

Phantom Read
  Jeśli możliwa jest zmiana wartości zwracanej przez zapytanie.

  .. note::

    Różnica między Non-Repeatable Read a Phantom Read jest dość ulotna,
    zasadniczo polega to na tym, że Phantom Read może wystąpić jeśli inna
    transakcja doda nowe dane.

  **Short example**:

  * T1 wykonuje zapytanie: ``SELECT AVG(value) FROM account WHERE ...GROUP BY ...``
  * T2 zapytanie: ``INSERT .... INTO account``
  * T2 jest komitowane
  * T1 wykonuje zapytanie: ``SELECT AVG(value) FROM account WHERE ...GROUP BY ...``

Write Skew
  Jest to anomalia w bazach MVCC, w której dwie transakcje (z których każda oddzielnie
  zostawia bazę w dobrym stanie) przenoszą bazę danych do niedozwolonego stanu.

  Mamy bazę danych banku, w której zamiast przechowywać saldo, przechowuje się 
  listę transakcji, a sumując ją uzyskuje saldo: ``SELECT SUM(t.value) FOR account .... INNER JOIN transaction as t ON ...``.
  Dodatkowo mamy ograniczenie, które zakłada, że saldo jest większe od zera.

  * Na początku transakcji konto A ma saldo 100PLN
  * T1 się zaczyna
  * T2 się zaczyna
  * T1 dodaje transakcje na  100PLN (co jest poprawne)
  * T1 Commits
  * Transackja T2 robi to samo (Co ciągle jest poprawne bo T2 nie widzi zmian
    wykonanych przez T2).

Dwie metody na ACID
*******************

Są dwie metody na zachowane ACID:

* Używanie zatrzasków (locków)
* Używanie MVCC


Poziomy Izolacji
****************

W ACID najłatwiej rozluźnić zasady izolacji. SQL definiuje takie poziomy izolacji:

Bazy dancyh z zatrzaskami
^^^^^^^^^^^^^^^^^^^^^^^^^

Zatrzask pozwala na oznaczenie danego wiersza jako zablokowanego
do odczytu lub zapisu. Jeśli transakcja A ma zatrzask na wierszu B do zapisu,
to żadna inna transakcja nie może uzyskać zatrzasku na tym wierszu. Jeśli ta
sama transakcja ma zatrzask do odczutu, to inne transakcje mogą uzyskać zatrzask
do odczytu, ale nie do zapisu.

Read Uncommitted
  W tym poziomie izolacji nie ma żadanych zatrzasków.

  Możliwe są wszystkie anomalie.

Read Commited
  W tym poziomie izolacji transackje nie widzą zmian wykonanych przez
  niezakończone transakcje, ale widzą zmiany wykonane przez transakcje
  zakończone.

  Zatrzaski zakładane są na:

  * Każdy wiersz, do którego się zapisuje;
  * Każdy odczytywany wiersz.

  Wiersze do zapisu są trzymane do końca transakcj, ale te do odczytu są
  trzymane do tylko na czas zapytania.

  Na tym poziomie są możliwe anomalie: Non-repeatable read oraz phantom read.


Repeatable Read
  W tym poziomie izolacji odczyt wiersza zawsze daje ten sam wynik.

  Zatrzaski zakładane są na

  * Każdy wiersz, do którego się zapisuje;
  * Każdy odczytywany wiersz.

  Zatrzaski są zwalniane dopiero pod koniec transakcji.

  Na tym poziomie jest możliwy: phantom read.

Serialized
  Najwyższy poziom izolacji. Nie możliwe są żadne anomalie odczytu.

  Transakcje wykonują się **tak jakby** wykonywały się jedna po drugiej.

  Zatrzaski zakładane są na

  * Każdy wiersz, do którego się zapisuje
  * Każdy odczytywany wiersz.
  * Każde zapytanie dodaje jeszcze zatrzask na zakres danych, który uniemożliwia
    wstawienie danych, które zmieniałyby jego wynik.

  Zatrzaski są zwalniane dopiero pod koniec transakcji.

Bazy danych oparte o MVCC
^^^^^^^^^^^^^^^^^^^^^^^^^

Takie bazy danych działają inaczej, niż te oparte na zatrzaskach, każda transakcja
widzi zawsze spójny obraz bazy danych, z chwili swojego rozpoczęcia.

.. note::

  Główna zaleta MVCC jest taka, że najczęściej, możliwy jest bezkolizyjny zapis
  równoległy i odczyt danego wiersza.


Fizyczna implementacja w Postgresql jest dość ciekawa:

Transakcje mają ID transakcji, dla ID transakcji zdefiniowano operator
mniejszości.

Każdy wiersz posiada kilka magicznych kolmn

``xmin``
  Id transakcji ``txid`` która dodała wiersz.

``xmax``
  Id transakcji ``txid`` która usunęła wiersz.

``cmin``, ``cmax``
  Numer wyrażenia SQL w ramach transakcji, która dodała lub usunęła wiersz.

.. note::

  Obecność magicznych kolumn pokazuje nam, że tworzenie **bardzo małyh tabel**
  w postgresql może być niewydajne.

Podstawowe operacje MVCC
^^^^^^^^^^^^^^^^^^^^^^^^

Dodanie wiersza
  Dodajemy wiersz z pustym ``xmax`` oraz z ``xmin`` równym id aktualnej transakcji.

Usunięcie wiersza
  Ustawiamy ``xmax`` na id aktualnej transakcji.

Uptate wiersza.
  Uptade jest parą Delete oraz Insert.

Widoczność danych
^^^^^^^^^^^^^^^^^

Transakcja widzi wiersz jeśli:

* ``xmin < txid`` (Wiersz został dodany w transakcji wcześniejszej. ).
* Transakcja ``xmin`` jest skomitowana (w przypadku poziomu izolacji Read Commited),
  lub ``xmin`` było skomitowane na początku transakcji ``txid``
  (pozostałe poziomy izolacji)
* Kolumna ``xmax`` jest pusta lub: ``xmax > txid`` (wiersz został usunięty
  przez transakcję po tej transakcji).

VACUUM
^^^^^^

Baza danych MVCC nie może usuwać wiersza z dysku od razu, musi on być dostępny,
aż wszystkie transakcje, które mogą go widzieć się zakończą.

Proces czyszczenia danych jest nazywany ``VACUUM``, i działa z grubsza automatycznie.

Poziomy Izolacji dla MVCC
^^^^^^^^^^^^^^^^^^^^^^^^^

Bazy danych MVCC pozwalają na uzyskanie takich samych poziomów izolacji do
bazy danych oparte na zatrzaskach. Możliwy jest jeden dodatkowy poziom izolacji


Snapshot Isolation
  W tym poziomie izolacji każda transakcja widzi stan bazy danych ze swojego początku.

  Pozwala ona na Anomalię Write Skew.

Bazy Danych NoSQL
-----------------

Ostatnio bardzo modne są bazy danych NoSQL, które dzielą się z grubsza na takie,
które:

* Przechowują dane trudne to dodania do modelu relacyjnego: np. dokumenty które
  mają być przechowywane pełnotekstowo.
* Mają poluzowane wymogi ACID, na przykład:

  1. Transakcje mają ograniczoną długość.
  2. Nie ma wymogu Durability.


Pojęcie skalowalności
*********************

Wydajność systemu
  To ilość transakcji w tym systemie może obsłużyć dany komputer.

Skalowalność
  Określa o ile wzrośnie wydajność systemu po dodaniu do niego kolejnych
  komputerów.

System może być bardzo wydajny i nie skalowalny, przykładem jest strona
Mailinator, która odbiera kilkaset e-maili na sekundę i działa na jednym
serwerze, w `obecnej architekturze <http://highscalability.com/mailinator-architecture>`__
nie ma możliwości podzelenia ruchu na wiele serwerów.

System może być mało wydajny i nie skalowalny. Jeśli zrobie system, który na jednym
serwerze obsłuży 10 maili na sekundę, ale który skaluje się perfekcyjnie (tj.
kolejne komputery dodane do klastra powodują liniowy wzrost ilości przetwarzanych
wiadomości), to po dodaniu 200 kompuerów do klastra osiągnę mozliwość przetwarzania
większej ilości e-maili, niż robi to mailinator. System będzie mało wydajny ale
skalowalny.

Problem z Durability
********************

Powiedzmy, że mamy klaster 10 baz danych (tj. 10 komputerów serwuje tę samą bazę danych).

Durability wymaga by po zakończeniu transakcji dane znalazły się na dysku
każdego z tych komputerów. Już sam zapis na dysk bardzo spowalnia proces
zakończenia transakcji, w klastrze należy jeszcze o fakcie zakończenia transakcji
poinformować wszystkie komputery.

Te problemy z Durability powodują, że systemy bazodanowe **trudno się skalują**,
tj. kolejne komputery dodane do klastra zwiększają jego wydajność w coraz
mniejszym stopniu.

Model Eventual Consistency
**************************

Bazy danych NoSql operują w modelu eventual consistency. W bazach SQL po zapisaniu
transakcji, mamy gwarancję, że stan wszystkich komputerów w klastrze jest spójny.

Bazy danych NoSQL gwarantują natomiast, że: "stan bazy danych będzie spójny kiedyś,
prawdopodobnie". Pozwala to np. odnoować transakcję, która została zapisana na
dysku tylko jednego serwera (który potem po jakimś czasie rozpropaguje dane dalej).

Dużo łatwiej skaluje się dane w modelu eventual consistency.

Transakcje w Django
*******************

.. code-block:: python

  from django.db import transaction

  with transaction.atomic():
    # Ten blok wykona się w transakcji
    # Transakcja zostanie skomitowana jeśli blok się zakończy
    # Jeśli z bloku poleci wyjątek tranzakcja zostanie odwołana.

Serwery asynchroniczne
----------------------

Mamy zasadniczo dwa rodzaje serwerów przetwarzających rządania HTTP:

1. Takie, które jednemu zapytaniu przypisują jeden wątek.
2. Takie, które z jednego wątku wykonują wiele zapytań.

Django zawsze działą w systemie synchronicznym, czyli jednemu zapytaniu
przypisuje się jeden wątek.

Dla pewnych rodzajów serwerów, serwery synchroniczne są nie wydajne, a serwery
asnychroniczne mogą być wydajniejsze o kilkaset razy (tj. mogą przetworzyć
kilkaset razy więcej zapytań).

Komunikacja blokująca
*********************

Komunikacja blokująca działa tak, że kiedy chcemy wykonać jakąś operację 
związaną z odczytem bądź zapisem danych
(z dysku, z bazy danych, z gniazda sieciowego), to akualny wątek blokuje się
do czasu jej zakończenia.

Na przykład jeśli wykonujemy zapytanie, to aktualny
wątek czeka aż nie otrzyma odpowiedzi.

Okazuje się, że dla "typowych" aplikacji webowych wątek przez większość czasu
"czeka" na zakończenie komunikacji, w tym czasie procesor może przełączyć się
na inny wątek i go wykonywać.

Serwery asynchroniczne
**********************

W serwerach synchroncznych mamy tyle wątków co połączeń HTTP, a w serwerach
asynchronicznych tyle wątków co rdzeni (każdy wątek obsługuje wiele zapytań).

Zyski są takie:

1. Każdy wątek zajmuje przynajmniej 1mb ramu, przy 1000 wątków robi się z tego
   gigabajt.
2. Przełączenie procesora między wątkami też zajmuje trochę czasu, w Internecie
   znalazłem, że jest to czas rzędu mikrosekundy.

   Dodatkowo przełączenie procesora między wątkami powoduje opróżnienie keszu
   procesora, co również zmniejsza wydajność.

Wady serwerów asynchronicznych:

1. Trudniej się je pisze.


Przykład:

Rozważmy serwer, który obsługuje N połączeń. Gdy dowolne z nich wyśle jedną linijkę 
tekstu linijka ta trafia do wszystkich polączonych::

  clients = set()

  async def handle_connection(self, reader:StreamReader, writer:StreamWriter):
      self.clients.add(writer)
      while True:
        data = await reader.readline()
        for w in self.clients:
          if w == writer:
            continue
          w.write(data)
          await w.drain()
        if not data:
          if writer in self.clients:
            self.clients.remove(writer)
            try:
              writer.write_eof()
            except OSError:
              pass # Sometimes it explodes if socket was closed very soon, didn't investigate
            return

.. note::

  Dokładne wyjaśnienie na zajęciach :)

Rozwiązanie pośrednie
*********************

Możliwe jest rozwiązanie pośrednie z użyciem tzw. zielonych wątków,
w którym jeden wątek systemu operacyjnego, obsługuje wiele zielonych wątków
w programie.

Przykładem języka, który obsłguje zielone wątki jest GO.
