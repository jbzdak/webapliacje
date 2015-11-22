Szablony Django i tworzenie ładnych stron WWW
=============================================


Formularze tworzone z Modeli
----------------------------

Powiedzmy, że mamy w bazie danych model ``Student``:

.. code-block:: python

  from django.db import models

  class Student(models.Model):

    name = models.CharField(max_length=100)
    pesel = models.CharField() # Validację dodamy później

    # Address
    street_name = models.CharField(max_length=100)

    # ...

oraz formularz:

.. code-block:: python

  from django.core import forms

  class StudentFoem(forms.Form):

    name = forms.CharField(max_length=100)
    pesel = forms. CharField() # Validację dodamy później

    # Address
    street_name = forms.CharField(max_length=100)

Te dwie klasy są bardzo podobne, w zasadzie na tyle podobne, że w sumie
powinna być możliwość automatycznego generowania formularzy, które mają
takie same pola jak modele.

Ogólnie: pewne rodzaje formularzy, zawsze będą bardzo podobne do modeli, Django
umożliwia więc generowanie takich formularzy automatycznie.

Przykład 1
**********

Rozważmy taki model:

.. code-block:: python

  class Address(models.Model):

    street_address = models.CharField(verbose_name="Street address", max_length=100)
    street_no = models.CharField(verbose_name="Street number", max_length=100)
    zip_code = models.CharField(verbose_name="zip-code", max_length=10)
    city = models.CharField(verbose_name="City", max_length=100)
    voivoidship = models.CharField(verbose_name="Voivoidshio", max_length=100)

.. note::

  To które z ograniczeń wymuszać po stronie bazy danych, a które po stronie
  aplikacji jest sztuką --- w przypadku adresow, imion i nazwisk raczej
  pozostawiałbym weryfikację aplikacji, a nie bazie danych.

Tworzymy najprostszy formularz:

.. code-block:: python

  from django import forms

  from . import models

  class AddressFormA(forms.ModelForm):

    class Meta:
      model = models.Address
      exclude = ['id']

Ważne elementy:

* Formularz dziedziczy po klasie ``ModelForm``
* Wewnątrz formularza nie określiłem żadnych!
* Zdefiniowana jest również klasa ``Meta`` która określa że:

  * Formularz ten obsługuje model ``models.Address``
  * Zawiera on wszystkie pola **poza** polem z kluczem głownym.

Praca z formularzami
********************

Praca z formularzami ``ModelForm`` jest bardzo podobna do pracy z normalnymi
formularzami. Są następujące różnice:

* ``ModelForm`` udostępnia metodę ``save()``, która: zbiera dane z formularza
  i tworzy instancję odpowiedniego modelu, oraz zapisuje go w bazie danych.
* Przy tworzeniu instancji ``ModelForm`` mozna podać instancję modelu, i
  w takim wypadku formularz posłuży do edycji modelu.

Przykład widoku umożliwiającego dodawanie i edycję adresu
(proszę przeczytać dokładnie z komentarzami; jeśli czegoś nie rozumiecie
proszę koniecznie pytać na zajęciach).

.. code-block:: python

  def generic_address_view(request, address_id):
  # Tutaj przechowujemy edytowany adres. Jeśli adres jest dodawany to pole to
  # jest Nonem, w przypadku edycji jest to edytowany adres.
  instance = None
  # Jeśli przekazano address_id (id edytowanego adresu) to pobieramy go
  # z bazy danych.
  if address_id is not None:
    # funkcja get_object_or_404 pobiera obiekt z bazy danych, a jeśli go nie
    # ma w bazie powoduje zwrócenie statusu 404 (rzucając odpowiedni wyjątek)
    instance = get_object_or_404(models.Address,pk=address_id)
  if request.method == 'POST':
    # Jeśli metodą jest ``POST`` to przekazujemy do formularza dane z metody POST
    # oraz edytowaną instncję. Jeśli instance jest None oznacza to że dodajemy
    # nowy adres a nie edytujemy stary.
    form = AddressFormA(request.POST, instance=instance)
    if form.is_valid(): # Jeśli formularz jest OK
      form.save()       # Zapisujemy model
      return redirect("form-list") # Przekierowanie
  elif request.method == 'GET':
    form = AddressFormA(instance=instance)
  else:
    return HttpResponse(status=405)

  # Tutaj dojdziemy w dwóch wypadkach:
  # 1. Zapytanie jest GET
  # 2. Zapytanie jest POST ale formularz wypełniono nieprawidłowo

  ctx = {'form': form}

  # Wyświetlamy odpowiedź
  return render(request, "zaj7app/add_form.html", ctx)


Nadpisywanie pól w formularzach
*******************************

O ile bardzo ogólna definicja pól w modelu może mieć sens, o tyle formularz
powinien sprawdzać czy pole kod pocztowy zawiera dane w poprawnym formacie.

Do sprawdzenia danych zastosujemy pola formularzy z biblioteki
``django-localflavor``, która zawiera pola formularzy potrafiące sprawdzać
dane specyficzne dla danego kraju.

Przykładowo:

.. code-block:: python

  from localflavor.pl.forms import PLPESELField, PLPostalCodeField, PLProvinceSelect

  class AddressFormB(forms.ModelForm):

    zip_code    = PLPostalCodeField(max_length=100)
    voivoidship = forms.CharField(max_length=100, widget=PLProvinceSelect())

    class Meta:
      model = models.Address
      exclude = ['id']

W przykładzie tym nadpisałem pole ``zip_code`` i ustawiłem je pole ``PLPostalCodeField``,
które weryfikuje format wprowadzonych danych.

Wprowadzenie do HTML
--------------------

Dobrym zwyczajem jest oddzielenie zawartości od sposobu jej przezentowania,
ma to następujące zalety:

* Łatwo jest zmienić wygląd strony, bez modyfikacji jej zawartości
* Strona jest czytelna maszynowo --- co ułatwia np. prawidłowe jej indeksowanie
  w wyszukiwarkach.

.. note::

  W dobrym tonie jest używanie `semantycznych tagów HTML5 <http://diveintohtml5.info/semantics.html#new-elements>`__,
  jeśli ktoś jest zainteresowany to dobrze jest się z tym zapoznać.

Elementy HTML oraz ich własności
********************************

Każdy element html ma trzy podstawowe własności:

* Rodzaj elementu. Na przykład element ``<p></p>`` ma rodzaj ``p``.
* Id elementu, jest ono definiowane za pomocą atrybutu ``id``. Na przykład
  ``<p id="important-par"></p>``. Id są unikalne --- tj. tylko jeden element na
  stronie może mieć dane id.
* Listę klas. Każdy element może mieć wiele klas na przykład: ``<p class="foo bar"></p<``
  oznacza że element ma klasę foo oraz bar.

Uwaga: klasy i id nie mają znaczenia **same w sobie**, to znaczenie nadaje im
aplikacja, kod javascript oraz plki CSS>


Podstawowe elementy w HTML
**************************

``<p>``

  Definiuje paragraf tekstu

``<ol>``

  Lista numerowana, zawiera wewnątrz tagi ``<li>`` określające kolejne elementy
  listy. Np.

  .. code-block:: html

    <ol>
      <li>Pierwszy element</li>
      <li>Drugi</li>
    </ol>

``<em>``, ``<strong>``

  Powodują podkreślenie danego fragmentu tekstu. ``<strong>`` podkreśla mocniej
  niż ``<em>``.

  Na przykład:

  .. code-block:: html

    <p> HTML5 nie pozwala np. na jawne podkreślenie tekstu kursywą,
    bądź wyboldowaniem, nie jest to jednak <em>brak</em> w standardzie
    a <strong>świadoma decyzja projektowa</strong>. </p>

``<h1>``, ``<h2>``

  Nagłówki


Język CSS
*********

Język CSS służy do definiowania "wyglądu strony" składa się on z dwóch elementów:

* Języka selektorów --- czyli czegoś co wybiera elementy.
* Języka własności --- który pozwala modyfikować własności elementów.

Arkusz styli CSS wygląda mniej-więcej tak:

.. code-block:: css

    selektor {
        atrybut: wartość;
        atrybut: wartość;
        atrybut: wartość;
    }


Gdzie ``selektor`` jest selektorem, a wewnątrz nawiasów ``{}`` mamy własności
obiektów wybranych przez ten selektor. Na przykład:

.. code-block:: css


    h1 {
        background-color: black;
        color: white;
        font-size: 20px;
    }

Selektory CSS
*************

Wybieranie po rodzaju tagu

    Selektor równy nazwie tagu wybiera wszystkie tagi danego typu:

    .. code-block:: css
        h1 {
            background-color: black;
        }

Wybieranie klasy

    By wybrać wszystkie tagi mające jedną z klas należy wpisać: ``.nazwa-klasy``
    (nazwa klasy poprzedzona kropką).

    .. code-block:: css

        .slide {
            padding: 5px;
        }

Wybieranie po id:

    By wybrać tak po ID należy wpisać ``#wartość-id``.

Selektory można łączyć, czyli by wybrać wszystkie nagłówki o klasie foo
należy napisać: ``h1.foo``.

Selektorami CSS można też wybierać tagi w hierarhii, na przykład by wybrać
tagi ``strong`` wewnątrz nagłowka ``h1`` należy napisać selektor: ``h1 strong``.


.. note::

    Opis jest dość pobieżny i osoby bardziej zainteresowane powinny doczytać :)

Podstawowe własności CSS
************************

Na przykładzie:

.. code-block:: css

    .foo{
        color: #ffffff; /* kolor pierwszego planu --- np. fontów, symboli 8*/
        background-color: #000000; /* kolor tła */
        font-family: "Book Antiqua", sans-serif; /*czcionka*/
        font-weight: 800 ; /*stopień wytłuszczenia */
        font-style: italic; /* italiki */
        text-decoration: underline; /* podkreślenia, przekreślenia */
        width: 50px;
        height: 50px;
        padding-left: 5px; /* odległość między lewym brzegiem pudełka a lewą ramka*/
        border-left-width: 2px;  /* grubość lewej ramki*/
        margin-left: 5px; /* odległość do obiektu po lewej */
        /* analogicznie marigin-right */
        /* każde sensowne IDE ma wsparcie dla code completion w plikach css. USE IT*/
    }


Załączanie statycznych plików do aplikacji Django
-------------------------------------------------

Pliki CSS oraz javascript są statycznymi plikami, django ma dość dobre wsparcie
do serwowania statycznych plików.

By serwować statyczne pliki należy:

* Stworzyć w swojej aplikacji katalog static.
* Umieścić wszystkie pliki wewnątrz katalogu static
* W szablonach użyć tagu ``{% static "ścieżka do zasobo" %}``.

Przykładowo, moja aplikacja wygląda tak::

    zaj7/
      static/
        zaj 7/
          styles.css
      templates/
      models.py
      forms.py

By załączyć plik ``styles.css`` na mojej stronie muszę napisać::

    <link rel="stylesheet" href="{%static "zaj7/styles.css" %}">

.. note::

    Podana recepta działa za tylko w środowisku developerskim --- na produkcji
    należy zastosować inne rozwiązania (które będą podane przy rozdziale o
    deploymencie)

Załączanie statycznych plików do strony WWW
-------------------------------------------

By dodać plik css do strony www należy dodać taki tag::

    <link rel="stylesheet" href="adres pliku">

Tag ten należy umieścić **wewnątrz tagu head**.

By dodać plik z javaskryptem do strony WWW należy dodać tag o treści::

      <script src="adres"></script>

Plik ten należy umieścić wewnątrz tagu body na samym końcu strony.

.. note::

    Pliki CSS umieszczamy na początku strony by strona była ostylowana podczas
    ładowania. Pliki JS na końcu ponieważ przeglądarki wstrzymują pracę nad
    stroną na czas ładowania plików z javaskryptem, uznaje się zatem że strona
    powinna już wtedy wyświetlać jakąś treść, by użytkownik nie gapił się 
    na biały ekran.

Generowanie stron WWW których wygląd nie woła o pomstę do nieba
---------------------------------------------------------------

Tutaj zasadniczo rozwiązanie można streścić w jednym zdaniu: "Proszę używać 
biblioteki Bootstrap", jest to zestaw styli i javaskryptu dostarczonego przez
firmę Twitter i rozwijanego na zasadach open-source.

Przykładowo ta strona korzysta z szablonu bootstrapa, dokładniej rzecz biorąc
``tego szalonu <http://getbootstrap.com/examples/blog/>``__.

.. note::

    Jest to prawdopodobnie jedyna część zajęć na której będę Was zachęcał do
    kopiowania kodu.


Tworzenie szablonów django które jest łatwo edytować
----------------------------------------------------

Jak zauważyliście na poprzednich zajęciach każdy szablon zawierał trochę
tego samego kodu, np:

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Address list</title>
    </head>
    <body>
        Zmiany były tu
    </body>
    </html>

Jeśli zapragnąłbym dodać do strony nowe style, musiałbym je dodać do wielu
szablonów na raz. Sytuacja taka jest niepożądana, więc szablony django oferują dziedziczenie.

Szablon base.html
*****************

Zasadniczo strona najczęściej zawiera szablon o nazwie ``base.html`` który
zawiera głowny szkielet strony, przykładowo (to jest przykład z jenego z moich
projetów). Szablon ten zawiera dołączoną bibliotekę bootstrap.

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/html">
      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="author" content="Jacek Bzdak <jbzdak@gmail.com>">

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css">
        <link rel="stylesheet" href="https://code.jquery.com/ui/1.11.4/themes/black-tie/jquery-ui.css">

        {% block additional-styles %}{% endblock %}

      </head>

      <body>
      {% block body %}

      {% endblock body %}
      {% block scripts-bottom %}
        <script src="https://code.jquery.com/jquery-2.1.3.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
        <script src="https://code.jquery.com/ui/1.11.4/jquery-ui.min.js"></script>

        {% block page-script-bottom %}{% endblock %}
        {% endblock %}
        </div>
      </body>
    </html>

W szablonie tym są nowe tagi ``{%block%}`` definiują one **bloki strony** i
są o tyle ważne, że pozwalają na zdefiniowanie mechanizmu dziedziczenia
szablonów. Tj. mając taką stronę mogę powiedzieć mechanizmowi szablomów Django:
"poproszę o stronę, która wygląda tak samo, ale wewnątrz bloku o nazwie body
jest taka treść". Tutaj uwaga: przez blok body mam na myśli ``{% block body %}``
a nie tag ``<body>``.


Mechanizm dziedziczenia w szablonach
************************************

Tutaj znów najłatwiej jest na przykładzie, to jest szablon login tego samego projektu:

.. code-block:: html
    {% extends "base.html" %}

    {% block additional-styles %}
    <link href="{{ STATIC_URL }}css/signin.css" rel="stylesheet">
    {% endblock %}

    {% block body %}

    <div class="container">

      <form class="form-signin" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button class="btn btn-lg btn-primary btn-block" type="submit">
            Logowanie!
        </button>
      </form>

    </div>
    {% endblock %}

Pierwszym tagiem jest tag ``{% extends "base.html" %}``, który mówi: 'Drogie
Django mieć szablon taki sam jak "base.html", ale z nadpisanymi takimi blokami'.
Dalej jest lista bloków do nadpisania.



