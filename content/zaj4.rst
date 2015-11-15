Zajęcia 4: Zadania
==================

:date: 2015-11-6
:tags: zaj4, zadania
:category: zadania

Do przygotowania przed zajęciami (jeśli macie własny komputer)
--------------------------------------------------------------

1. Zainstalować Pythona 3.4+
2. Stworzyć virtualne środowisko z zainstalowanym Django.

Zadanie na zajęcia
------------------

Kod statrowy do pobrania `stąd <downloads/calculator.zip>`__.

.. note::

  Aplikacja będzie testowana **automatycznie**, więc wszystkie instrukcje jakie
  podaje należy wypełniaź **dokładnie** :)

Korzystając z udostępnionego kodu stworzyć serwis mający prostą funkcjonalność:

1. Po wysłaniu zapytania ``GET`` na adres ``/calculate`` otrzymujemy formularz,
   formularz ten zawiera trzy pola, pola o nazwie ``x`` oraz ``y`` zawierają 
   liczbę, ``operation`` natomiast znak (jeden z: ``+``, ``-``, ``*``, ``/``, ``//``).

   Formularz wysyła zapytanie ``POST`` na adres ``/calculate``, zapytanie zawiera
   trzy parametry: x, y, operation.
2. Jeśli zapytanie ``POST`` zawiera błąd (brak parametru, niepoprawna wartość)
   powinien się wyświetlić pusty formularz i wiadomość: "Zła wartość parametru".
3. Jeśli zapytanie ``POST`` jest poprawne system powinien zwrócić stronę z
   informacją: ``Result of {x}{operation}{y} is {res}``, na przykład:
   ``Result of 3+3 is 6``.
4. We wszystkich powyższych przypadkach serwer powinien zwracać status ``200``.

   .. note::

     By wybrać status odpowiedzi mozna przekazać do odpowiedzi parametr ``status_code``
     np. ``return HttpResponse(status_code=405)``.

4. Jeśli na adres ``/calculate`` zostanie zwrócone zapytanie inne niż ``GET`` lub
   ``POST`` system powiniene zwrócić status ``405``.

