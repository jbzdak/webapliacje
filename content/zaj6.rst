Zajęcia 6: Zadania
==================

:date: 2015-11-23
:tags: zaj6, zadania
:category: zadania


.. note::

  Problemy z zajęć:

  1. Tworzenie projektu: django-admin startproject (z virtualnego środowiska)
  2. Tworzenie aplikacji: ./manage.py startapp
  3. Do renderowania widoków (ze względu na CSRF) należy użyć funkcji:

     .. code-block:: python

        from django.shortcuts import render

        def view(request):
          ...
          return render(request, 'nazwa/widoku.html', {'form': form}

    Wynika to z tego że tag ``{% csrf_token %}`` musi posiadać w kontekście
    zmienną ``csrf_token``, która jest dodawana automatycznie.

  4. Aplikajcę należy dodać do listy aplikacji ``INSTALLED_APPS`` w
     ``settings.py``.

  5. Do weryfikacji numerów pesel można użyć aplikajci: ``pip install django-localflavor``,
     a w niej ``localflavor.pl.forms``

Zadaniem na zajęcia jest stworzenie trzech aplikacji, które mają tą samą 
funkcjonalność, kolejne aplikacje będą coraz mniej korzystały z narzędzi Django.

Cele zadania:
-------------

Aplikacja posiada trzy widoki:

* Widok logowania, w widoku tym pytamy nazwę użytkownika i hasło.
* Listę studentów (widoczną dla każdego)
* Stronę do dodawania studenta (widoczną dla zalogowanych)

Zachowania aplikacji:

* Student posiada takie dane jak: `imie i nazwisko` i `pesel` (sprawdzany)
* Dodawania studenta realizowany jest za pomocą Formularzy Django.
* Po wejściu na stronę dodania studenta osoba niezalogowana przenoszonona na stronę 
  logowania.

Zadanie na 3
------------

Do obsługi logowania korzystamy z systemu logowania Django, składa się on z
takich elementów. Działanie systemu logowania Django.

Model ``auth.User``
*******************

Model ten trzyma podstawowe dane o Użytkowniku, w tym:

* Imie i nazwisko
* Nazwę użytkownika
* Skrót hasła

By dodać startowego użytkownika możecie użyć komendy ``./manage.py createsuperuser``.

.. note::

  Komenda ta dodaje superużytkownika --- który ma bardzo duży poziom uprawnień,
  by stworzyć *zwykłego* użytkownika można użyć interfejsu administracyjnego
  Django, który będzie tematem następnych zajęć.

Logowanie użytkownika
*********************

By "zalogować" użytkownika w widoku należy:

.. code-block:: python

  from django.contrib.auth import authenticate, login

  def my_view(request):
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
          if user.is_active:
              login(request, user)
              # Redirect to a success page.
          else:
              # Return a 'disabled account' error message
              ...
      else:
          # Return an 'invalid login' error message.
          ...

Można tez skorzystać wbudowanego widoku: ``django.contrib.auth.views.login``.

Sprawdzanie czy użytkownik jest zalogowany
******************************************

Aplikacja ``django.contrib.auth`` domyślnie "dopina" do obiektu ``request``
zalogowanego użytkownika jako atrybut ``request.user``. Atrybut ten jest
instancją modelu ``django.contrib.auth.models.User``.

By sprawdzić czy użytkownik jest zalogowany należy więc:

.. code-block:: python

  from django.conf import settings
  from django.shortcuts import redirect

  def my_view(request):
      if not request.user.is_authenticated():
          return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

Zadanie na 4
------------

Aplikacja działa tak samo, ale nie korzysta z framewoeku ``django.contrib.auth``,
tylko:

1. Posiada własny model na użytkownika
2. Sprawdza hasło użytkownika
3. Przechowuje dane zalogowanego użytkownika w sesji.
4. Do obsługi sesji wykorzystujecie mechanizmy Django.
5. Tutaj musicie jeszcze dodać widok umożliwiający zakładanie konta.

Miejsce przechowywania danych o sesji
*************************************

Dane powiązane z sesją użytkownika mogą być przechowywane w wielu miejscach:

* Bazie danych
* Dysku twardym serwera
* W keszu aplikacji
* W plikach cookie po stronie użytkownika (pliki są poprawnie podpisane, ale nie
  są szyfrowane)

Każde z tych rozwiązań ma swoje wady i zalety. Domyślnie sesje zapisuje się w
bazie danych.

Jak działa mechanizm sesji
**************************

Mechanizm sesji "dopina" do obiektu ``request``
sesje aktualnego użytkownika (albo sesję nie powiązaną z użytkownikiem
jako atrybut ``request.session``). Atrybut ``session`` jest słownikiem
(który ma kilka dodatkowych metod, które na razie są nie ważne).

Co może być przechowywane w sesji
*********************************

W sesji (domyślnie) kluczami danych mogą być ciągi znaków, a wartościami:

1. Słowniki
2. Listy
3. boole, inty, floaty
4. Ciągi znaków

W jaki sposób logować użytkownika
*********************************

Algorytm logowania użytkownika:

1. Sprawdzamy czy podał prawidłowe hasło.
2. Dodajemy do sesji klucz np. ``logged_in_user_name`` o treści równej nazwie
   użytkownika.
3. Wywołujemy metodę ``request.session.cycle_key()``.

.. note::

  Metoda ``request.session.cycle_key()`` zmienia klucz sesji, zachowując wszystkie
  inne dane powiązane z sesją. Pozwala to na uniknięcie ataku:
  `session fixation <https://en.wikipedia.org/w/index.php?title=Session_fixation&oldid=691251608>`__.

Algorytm wylogowywania użytkownia:

1. Wywołujemy metodę ``request.session.flush()``, która usuwa wszystkie dane z sesji.

Algorytm sprawdzania czy użytkownik jest zalogowany:

1. Sprawdzamy czy sesja zawiera klucz: ``logged_in_user_name``
2. Sprawdzamy czy wartość tego klucza powiązana jest z istniejącym użytkownikiem.


Zadanie na 5
------------

Jak zadanie na 4, ale użytkownik przechowuje hasło za pomocą kryptograficznego skrótu.


Funkcja skrótu
**************

Funkcja skrótu to funkcja którą ma takie cechy:

1. Przyjmuje ciąg bajtów dowolnej długości.
2. Zwraca ciąg bajtów określonej dlugości.
3. Mając wejściowy ciąg znaków łatwo jest wykonać funkcję.
4. Mając ciąg wyjściowy trudno jest znaleźć jakikolwiek ciąg wejściowy dający
   ten sam ciąg wyjściowy. Formalnie: mając daną funkcję ``F(A) -> B``, oraz
   ustalone ``B``, trudno jest znaleźć dowolne ``C`` takie że ``F(C) -> B``.

Pojęcie Soli
************

Sól jest losowym ciągiem znaków, który jest przechowywany w sposób jawny w
bazie danych. Sól powinna być unikalna dla każdego użytkownika. Sól jest
potrzebna ponieważ funkcje skrótu są deterministyczne.

Powiedzmy że przechowujemy hasło użytkownika jako prosty wynik funkcji skrótu,
i mamy dwoch użytkowników o skrócie równym: `2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae`.

Wiemy wtedy że:

1. Użytkownicy ci mają to samo hasło
2. Jak wpiszecie w google frazę: ``2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae``
   dowiecie się co to za hasło :)

Kiedy do hasła dodana jest sól (która jest globalnie unikalna) to:

1. Dwaj użytkownicy o tym samym haśle, mają różne sole, więc w bazie znajdują się
   różne skróty ich haseł.
2. Bardzo proste hasła wymagają odrobiny pracy do odwrócenia.

Celem stosowania soli jest:

1. Utrudnienie łamania bazy haseł.
2. Ochrona użytkowników mających proste hasła.
3. Ochrona użytkowników którzy dzielą hasła między stronami.



Zapisywanie hasła użytkownika
*****************************

1. Użytkownik wpisuje swoje nowe hasło w formularz.
2. Losujemy nową sól, która jest zapisywana do bazy danych
3. Wyznaczamy wynik funkcji skrótu z ciągu znakow::

    salt + '$' + hasło

między stronami.

Sprawdzanie hasła użytkownika
*****************************

1. Użytkownik wpisuje swoje nowe hasło w formularz.
2. Pobieramy sól z bazy danych
3. Wyznaczamy wynik funkcji skrótu z ciągu znakow::

    salt + '$' + hasło

4. Sprawdzamy czy wynik działania funkcji skrótu jest zgodny z tym zapisanym
   w bazie danych.

Możecie użyć tych metod:

.. code-block:: python

  import os, hashlib, base64

  def generate_salt():
    return base64.b64encode(os.urandom(16)).decode('ascii')

  def calculate_password_hash(password, salt):
    return hashlib.sha256((salt + '$' + password).encode('ascii')).hexdigest()


