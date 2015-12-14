Wykład 8: Testowanie aplikacji, interfejs admina i inne
=======================================================

:date: 2015-12-07
:tags: zaj8, wykład, materiały
:category: materiały

.. note::

  Wykład do pobrania również w wersji PDF.

  .. raw:: html

     <a href="downloads/pdfs/wyk8.pdf">Wersja pdf tutaj</a>

Testowanie aplikacji
--------------------

Po co testować
**************

Koszty utrzymania
^^^^^^^^^^^^^^^^^

Zarządzający projektami informatycznymi twierdzą, że utrzymanie oprogramowania
kosztuje więcej niż jego napisanie, to jaka jest to zależność bardzo
zależy od specyfiki proramowania. Niektórzy mówią że napisanie kosztuje
20% a utrzymanie 80%, inni trochę inaczej.

Dla bardzo małych projektów zależność ta jest inna (ale z reguły utrzymanie jest
**droższe** od napisania).

.. note::

  Nie oznacza to, że zawsze priorytetyzuje się minimalizacje kosztu utrzymania,
  bardzo często aktualne ograniczenia budżetowe, dedlajny powodują zaciągnięcie
  tzw. *długu technicznego*.

Koszt naprawy błędu
^^^^^^^^^^^^^^^^^^^

Koszt naprawy błędu (Buga) zmienia się w funkcji czasu wykrycia błędu.

1. Jeśli błąd w danej funkcjonalności odkrył programista w trakcie pisania
   funkcjonalności błąd jest bardzo tani do naprawy.
2. Jeśli błąd odkrył tester to koszt jest droższy (tester musi znaleźć błąd,
   znaleźć programistę który go naprawi, programista musi naprawić błąd ---
   co też nie jest proste, bo tester powie: "Okienko się nie pokazuje",
   tester musi potwierdzić działanie błędu).
3. Jeśli test odkryli klienci koszty są wielokrotnie wyższe: można utracić ich
   zaufanie; ew. poprawki trzeba rozdystrybuować do klientów (których czasem
   są miliony) itp.

Testy na ratunek
^^^^^^^^^^^^^^^^

Testy są jednym z narzędzi które zmniejszają koszty utrzymania oprogramowania,
ponieważ pozwalają na automatyczne testowanie poprawności jego działania.

Programista po dokonaniu zmian w aplikacji uruchamia testy, które sprwadzają 
poprawne działanie po zmianach, w praktyce pozwala to na:

1. Znaczne zmniejszenie ryzyka wprowadzenia błędów do już istniejącej
   funkcjonalności (tzw. regresji)
2. Bardzo podnosi komfort pracy osoby wdrażającej oprogramowania, bo ryzyko
   problemów jest niższe.
3. Powoduje, że większość błedów wykryje programista (raczej: wykryją testy)
   podczas pracy nad funkcjonalnością: co powoduje że koszt naprawy błędu
   jest minimalny.

Rodzaje testów
--------------

.. note::

  W literaturze znajduje się bardzo różne klasyfikacje testów (sam temat jest
  relatywnie nowy ma może 15 lat), więc latwo znajdziecie inną klasyfikację.


Testy jednostkowe
*****************

Co testujemy
^^^^^^^^^^^^

Są to testy, które powinny testować **jeden komponent**, w **izolacji**
od innych.

Zasadniczo testuje się działanie API danego komponentu.

Zewnętrzne zależności testowanego komponentu są mockowane, tj.
przedstawiane są sztuczne elementy, stworzone na potrzeby testu, które mają 
taki sam interfejs API jak dany kompoment.

.. note::

  Przykładowo: część aplikacji w Django korzysta z funkcjonalności wysłania
  e-maili, podczas testów mogą one skorzystać ze specjalnego backendu wysyłającego
  e-maile, który zamiast je wysyłać zapisuje je do specjalnej listy.

  Testy w takim wypadku mogą sprawdzić czy i jakie wyadomości program wysysłał,
  taki backend wysyłający e-maile jest przykładem mocka.

Czas i miejsce wykonania
^^^^^^^^^^^^^^^^^^^^^^^^

1. Wykonywać się bardzo szybko, najlepiej w ciągu raczej sekund niż minut.
2. Wykonuje je sam programista na swoim komputerze.
3. Wykonuje się je **przed skomitowaniem zmian do repozytorium**.
4. Wykonywane są kilkaset razy dziennie (niektóre IDE pozwalają na automatyczne
   uruchamianie testów jednostkowych po każdej zmianie w kodzie)
5. Testowane są zmiany każdego programisty oddzielnie (testowany jest każdy komit
   oddzielnie)

Zalety i wady
^^^^^^^^^^^^^

Zalety:

1. Można łatwo uruchomić w trybie debugu
2. Bardzo łatwo zlokalizować defekt (wiemy że winny jest testowany komponent)
3. Łatwe do napisania

Wady:

1. Nie są w stanie stwierdzić że dwa komponenty się ze sobą dogadają.

Testy Integracyjne
******************

Co testujemy
^^^^^^^^^^^^

To czy komponenty zastosowane razem działają poprawnie, tutaj też raczej testuje
się API niż interfejs użytkownika.

Testy jednostkowe są w stanie (z dużą dozą pewności) stwierdzić,
że dany komponent dziala poprawnie. Nie są w stanie natomiast stwierdzić że:

1. API dwóch komponentów jest kompatybilne (czyli: dwa komponenty razem się ze
   sobą dogadają) --- każdy testowany jest osobno.
2. Nie ma jakichś zależności bezpośrednio nie wyrażonych w API, które powodują 
   problemy z integracją.

Do sprawdzenia takich zależności stosuje się testy integracyjne.

Czas i miejsce wykonania
^^^^^^^^^^^^^^^^^^^^^^^^

1. Mogą być wolniejsze, ale ciągle powinny wykonywać się raczej w ciągu minut
   niż godzin.
2. Wykonuje je raczej sam programista na swoim komputerze.
3. Wykonywane są kilka razy dziennie.
4. Testowane są zmiany każdego programisty oddzielnie (testowany jest każdy komit
   oddzielnie)

Zalety i wady
^^^^^^^^^^^^^

Zalety:

1. Można uruchomić w trybie debugu (choć często jest to trudniejsze
   niż w jednostkowych)
2. Relatywnie łatwo zlokalizować defekt (choć trudniej niż przy jednostkowych)

Testy systemowe
***************

.. note::

  Powiązanym pojęciem są testy behavioralne.


Co testujemy
************

Testy te testują cały system na raz (albo raczej: możliwie zbliżoną do systemu
produkcyjnego replikę).

Testuje się raczej zachowania danego systemu niż działanie poszczególnych API,
np. testy systemowe często symulują działanie użytkownika klikającego w
przeglądarkę.

Można też testować API wystawiane przez system, ale z założeniem że testuje się 
**zachowanie systemu jako całości**.


Czas i miejsce wykonania
************************

1. Są wolne, mogą wykonywać się godzinami.
2. Wykonuje je raczej dedykowany system CI.
3. Często testowany jest "stan projektu po dniu pracy"

Zalety i wady
*************

Zalety:

1. Dają gwarancję że system działa "od strony użytkownika" (pozostałe rodzaje
   testów tej gwarancji nie dają)!

Wady:

1. Relatywnie trudno zlokalizować defekt (bo informacja może być ogólna),
   na poziomie: "Lista produktów zawiera produkty o złej cenie".
2. Czas wykonania.

Testy akceptacyjne
******************

Testy te robi klient przed odebraniem projektu. Mogą być one mniej lub
bardziej dokładne.

1. Często nie są zautomatyzowane (czasem są)
2. Jeśli są zautomatyzowane powinny wykonywać się w czasie poniżej 16 godzin
   (jeśli wyślesz kod przed wyjściem z pracy, następnego dnia rano masz wyniki :))
3. Wykonuje je dedykowany system CI.
4. Często testowany jest "stan projektu po dniu pracy"
5. Relatywnie trudno zlokalizować defekt


.. note::

  Są inne rodzaje testów, np. fuzz testing, w którym aplikację zarzuca się
  nonsensownymi danymi. Fuzz testing ma mniejsze zastosowanie dla aplikacji WWW,
  ale jest przydatny np. do testowania bezpieczeństwa kernala i sterowników.

Systemy CI
----------

Zasadniczo testy są o tyle przydatne, o ile ludzie je wykonują. Programiści nie
lubią wykonywać testów. Dlatego stworzono systemy CI które:

1. Pobierają każdą zmianę z repozytorium
2. Budują projekt
3. Uruchamiają wszystkie testy (lub wszystkie testy nie systemowe)
4. Informują programiste o tym czy testy przeszły.

Ci mogą też robić inne rzeczy:

1. Odrzucać zmiany jeśli "testów jest mniej"
2. Odrzucać zmiany jeśli kod nie spełnia wymogów formatowania

Piramida testów
---------------

Piramida projektów zwinnych
***************************

1. Najwięcej powinno być testów jednostkowych --- musi być ich najwięcej,
   ponieważ wykonują się one najszybciej, i umożliwiają najłatwiejsze naprawienie
   błędu.
2. Mniej powinno być testów integracyjnych --- są one ważne bo sprawdzają działanie
   komponentów razem, ale skoro mamy dużo testów jednostkowych, to integracyjne
   mają mniej rzeczy do sprawdzenia.
3. Najmniej testów systemowych --- testy systemowe są w zasadzie wisienką na torcie.

Piramida projektów tradycyjnych
*******************************

1. Najwięcej testów systemowych --- przecież chcemy testować system tak jak używa
   go użytkownik. Do tego automatyczne testy UI piszą testerzy, którzy nie wiedzą
   jak ma działać każdy komponent, ale wiedzą jak ma dzialać cała aplikacja.
2. Pozostałe testy są w zasadzie niepotrzebne

Moja piramida dla małych projektów
**********************************

Jeśli projekt jest mały, pracuje nad nim mały zespół, może udać się taka piramida:

1. Trochę testów jednostkowych --- ale tylko do najbardziej skomplikowanych
   części aplikacji.
2. Testy systemowe, które sprawdzają czy całość działa razem.

Pisanie testów w Django
-----------------------

.. note::

  Django ba **świetną dokumentację**, naprawdę warto ją przeczytać:
  https://docs.djangoproject.com/en/1.9/topics/testing/

Podstawy
********

Testy powinny znajdować się w pliku ``tests.py``. Testy są klasami
dziedziczącymu po ``django.test.TestCase``, dla osób znających Pythona,
jest to klasa dziedzicząca po ``TestCase`` z frameworku ``unittest``.

Wewnątrz tej klasy są pewne specjalne metody:

1. Każda metoda zaczynająca się od ``test`` jest testem i zostanie uruchomiona.
2. Metoda o nazwie ``setUp`` zostanie uruchomiona przed każdym testem (przed
   każdym testem baza danych jest pusta).

   Głównym zadaniem ``setUp`` jest dodanie do bazy wymaganych przez testy obiektów.
3. Metoda o nazwie ``tearDown`` zostanie uruchomiona po każdym teście, jej
   zadaniem jest "czyszczenie" po teście wszystkich zasobów poza bazą danych
   (te są czyszczone automatycznie).

.. note::

  Są jeszcze metody: ``setUpClass`` i ``tearDownClass``.

Po czym wiemy że test się udał
******************************

Mówimy że test się powiódł, jeśli nie rzucił on wyjątku.

Framework ``unittest`` dostarcza tzw. asercje, czyli funkcje które rzucają wyjątek
gdy jakiś wyjątek jest niepoprawny.

Wykonywanie zapytań
*******************

Do wykonywania zapytań służy klasa ``django.test.Client``, pozwala ona na:

1. Wykonywanie zapytań HTTP
2. Każda jej instancja pamięta ciastka przesłane przez server.

Przykład testu:

.. code-block:: python

  class TestFor3(TestCase):

    def test_for_empty_list(self): # Opisowa nazwa
      c = Client()
      response = c.get("/index/") # Wykonujemy zapytanie http
      # Sprawdzamy czy server odpowiedział statusem 200
      self.assertEqual(200, response.status_code)
      # Sprwadzamy czy zawartość jest odpowiednia
      # Jeśli nie jest leci wyjątek :)
      self.assertIn('No posts to show', response.content.decode("utf-8"))

Testowanie w Django
-------------------

Na co pozwala framework Django
******************************

Django posiada własny system testów, który pozwala na:

1. Testowanie jednostkowe aplikacji.
2. Proste testy integracyjne (jeśli sprawdzamy komponenty należące do jednego
   projektu).

Framework testów Django pozwala na przetestowanie:

1. Zachowań obiektów typu: modele, managery (to są unittesty)
2. Wybierania danych z bazy danych
3. Wykonywania zapytań HTTP i testowanie ich działania (np. czy dane zapisały się do bazy,
   czy HTML zawiera informację o błędach).

Framework testów Django nie pozwala na:

1. Testowanie poprawności działania kodu Javascript.
2. Testowanie wyglądu stron WWW.


.. note::

  Do testowania powyższych dwóch rzeczy (owszem można to robić) używa się
  rozwiązań, takich jak Lettuce i Selenium, jednak ja sam nigdy nie musiałem
  ich używać.

Co gwarantuje framework Django
******************************

Główną funkcjonalnością frameworku testów Django jest zarządzanie bazą danych,
w taki sposób by przed każdym testem baza danych:

1. Zawierała wszystkie tabele (uruchomiono wszystkie migracje)
2. Była pusta (zawiera dane jeśli migracje je wstawiły, ale nie zawiera danych
   które wstawiały inne testy).


Interfejs administracyjny
-------------------------

Django posiada (bardzo łatwy do wykonania) interfejs administracyjny, pozwalający
na zarządznie danymi w bazie **przez administratora**.

Do czego admin się nadaje:

1. Do udostępnienia administracji stroną, dla technicznych administratorów.

Do czego admin się nie nadaje:

1. Do udostępnienia użytkownikom końcowym --- model uprawnień nie pozwala na
   powiedzenie: użytkownik ma uprawnienia do modyfikacji np. "swoich postów".
2. Do udostępniania osobom nietechnicznym --- bardzo łatwo jest pisać 
   interfejsy admina, jest on też **bardzo elastyczny**, ale nie na tyle
   elastyczny by udostępnić go osobom którym nie wyjaśni się pojęcia np.
   **klucza obcego**.

Model uprawnień Django
**********************

Django posiada wbudowany system uprawnień, który pozwala na powiedzenie:

1. Ten użytkownik ma uprawnienia do *kasowania*, *dodawania* lub *edycji*,
   instancji danego modelu. Np. Edytor może
2. Nie pozwala on (w aktualnej wersji) na wyrażenie że: ten użytkownik może
   edytować, tą instancję tego modelu a innych nie.

Użytkownik może wejść na panel administracyjny jeśli:

* Jego konto jest aktywne
* Ma zaznaczone pole ``is_staff``

Użytkownik widzi listę encji z danego modelu jeśli ma jakiekolwiek uprawnienia
do tego modelu.

Uruchomienie panelu administracyjnego
*************************************

Panel administracyjny jest uruchomiony domyślnie, by go włączyć starczy w
głównym pliku ``urls.py`` zostawić takie mapowanie:

.. code-block:: python

  from django.contrib import admin

  urlpatterns = [
      url(r'^admin/', include(admin.site.urls)),
  ]


Przykład
********

Początek
^^^^^^^^

Po stworzeniu nowego projektu, panel administracyjny będzie zawierał możliwość:

1. Dodawania użytkowników
2. Dodawania grup użytkowników
3. Dodawania użytkownikom

Główna strona interfejsu admina wygląda tak:

.. figure:: static/wyk8/admin-czysty.png
  :width: 80%

  Główna strona interfejsu admina

Model i admin
^^^^^^^^^^^^^

Dodajmy nową aplikację o nazwie ``zaj8app`` z takim modelem:

.. code-block:: python

  class Student(models.Model):

    name  = models.CharField(max_length=100)
    e_mail = models.EmailField()


.. note::

   Dodajemy ją do ``settings.INSTALLED_APPS`` oraz:
   ``manage.py makemigrations`` i ``manage.py migrate``.

   Dodajemy też superużytkownika: ``./manage.py createsuperuser``.

.. note::

  Na bardzo dużym marginesie: najprostszą metodą na przechowywanie imienia osoby
  jest podanie jej długiego pola tekstowego. Nie każda kultura `używa
  nazwisk <http://www.w3.org/International/questions/qa-personal-names>`__.

Do pliku ``admin.py`` w aplikacji ``zaj8app`` dodajemy klasę:

.. code-block:: python

  # To jest tzw. dekorator, mówi on że klasa StudentAdmin opisuje interfejs
  # admina dla modelu Student
  @admin.register(models.Student)
  class StudentAdmin(admin.ModelAdmin):
    pass

Klasa ta nie robi w zasadzie nic --- wszystkie ustawienia Admina są domyślne,
tak skonfigurowany Admin pozwala na:

1. Dodanie i edycję studenta
2. Wyświetla (bezużyteczną na razie) listę studentów.

.. figure:: static/wyk8/default-list.png
  :width: 80%

  Lista studentów

.. figure:: static/wyk8/default-add.png
  :width: 80%

  Dodawanie studentów

.. figure:: static/wyk8/default-add-err.png
  :width: 80%

  Dodawanie studentów (walidacja)


Zmiana zachowania listy 1
^^^^^^^^^^^^^^^^^^^^^^^^^

Powiedzmy że w liście chcemy wyświetlać imie i nazwisko studenta, oraz
jego e-mail w formacie ``j...@gmail.com``.

.. code-block:: python

  # To jest tzw. dekorator, mówi on że klasa StudentAdmin opisuje interfejs
  # admina dla modelu Student
  @admin.register(models.Student)
  class StudentAdmin(admin.ModelAdmin):

    # Te pola będą wyświtlane w liście.
    # Mogą tu być:
    # 1. Pola modelu
    # 2. Zeroargumentowe funkcje na modelu
    # 3. Jednoargumentowe funkcje na adminie
    list_display = ('name', 'masked_e_mail')

    def masked_e_mail(self, obj):
      # obj to edytowany student
      email = obj.e_mail
      at = email.rindex('@')
      return email[0] + ('.' * (at-2)) + email[at:]


.. figure:: static/wyk8/list-fixed.png
  :width: 80%

  Dodawanie studentów (walidacja)

Zmiana zachowania widoku edycji
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Powiedzmy, że chcemy zmienić kolejność pól w widoku edycji, dodamey do modelu
zatem::

  fields = ('e_mail', 'name')

Dalej, chcemy generować numer albumu, który jednocześnie będzie kluczem głównym
modelu:

.. code-block:: python

  class Student(models.Model):

    nr_albumu = models.AutoField(primary_key=True)

    name  = models.CharField(max_length=100)
    e_mail = models.EmailField()

.. note::

  Ogólnie klucz główny nie powinien być widoczny poza bazą danych.

  Migracja zmieniająca klucz główny może być trudna dla Was do przeprowadzenia.

Pole z ``nr_albumu`` nie jest edytowalne, w tym celu należy dodać je do
``fields`` **oraz do** ``readonly_fields``::

  # To jest tzw. dekorator, mówi on że klasa StudentAdmin opisuje interfejs
  # admina dla modelu Student
  @admin.register(models.Student)
  class StudentAdmin(admin.ModelAdmin):

    # Te pola będą wyświtlane w liście.
    # Mogą tu być:
    # 1. Pola modelu
    # 2. Zeroargumentowe funkcje na modelu
    # 3. Jednoargumentowe funkcje na adminie
    list_display = ('nr_albumu', 'name', 'masked_e_mail')

    readonly_fields = ('nr_albumu',)

    fields = ('nr_albumu', 'e_mail', 'name')

    def masked_e_mail(self, obj):
      # obj to edytowany student
      email = obj.e_mail
      at = email.rindex('@')
      return email[0] + ('.' * (at-2)) + email[at:]

Więcej informacji o interfejsie administracyjnym:

* https://docs.djangoproject.com/en/1.8/ref/contrib/admin/


