Zajęcia 5: Zadania
==================

:date: 2015-11-9
:tags: zaj5, zadania
:category: zadania

Kod statrowy do pobrania `stąd <downloads/blog.zip>`__.

Zadanie polega na stworzeniu prostej aplikacji do blogowania.

Aplikacja spełnia następujące kryteria

**Na 3.0**

1. Stworzyliście aplikację o nazwie ``blog_app``, która jest dodana do
   ``settings.py``.
2. W aplikacji jest model o nazwie ``BlogPost``, który ma dwa pola:

   1. ``text`` zawierający treść posta
   2. ``posted_at`` zawierający datę wysłania posta.
   3. Pole ``posted_at`` zawiera chwilę czasu w której dodano posta, by je
      stworzyć mozna skorzystać z atrybutu ``auto_now_add`` konstruktora pola
      ``DateTimeField``, który powoduje że dane pole przy pierwszym zapisie
      do bazy danych otrzymuje wartość równą aktualnej dacie.

3. Na urlu ``/index`` wyświetla listę postów, oraz link do dodawania postów.
4. Jeśli nie ma postów do wyświetlenia na stronie musi pojawiać się napis:
   ``No posts to show``
5. Posty są wyświetlane od najnowszego do najstarszego.
6. Po wysłania zapytania ``GET`` na adres ``/edit`` pojawia się formularz
   do dodawania postów.

   Formularz ten ma pole ``text`` któego zawartość stanowi nowy tekst

7. Po wysłaniu zapytania ``POST`` na adres ``/edit``, jeśli pytanie to
   zawiera parametr ``text`` pojawi się nowy blog post.

   Zapytnaie to spowoduje przekierowanie użytkownika na adres z listą
   stron.

   .. note::

      Do wykonywania przekierowania służy kilka statusów, my w tym wypadku
      będziemy używać statusu ``302`` (choć poprawniejsze byłoby zastosowanie
      statusu ``303``).

      Do zwrócenia odpowiedzi z przekierowaniem służy w django metoda
      ``redirect``.

      .. code-block:: python

        def some_view(request):
          from django.shortcuts import redirect
          return redirect("/new-url")

**Na 4.0**

1. Jeśli w formularzu ``/edit`` nie będzie wypełnionego tekstu, powinienem ponownie
   dostać formularz do wypełnienia, ale z dodatkową informacją o błędzie:
   ``Please add post text``.

   Przez niewypełnione pole ``text`` rozumiem:

   * Brak parametru ``test`` w zaptaniu POST
   * Parametr ``text`` będący pustym ciągiem znaków
   * Parametr ``text`` będący ciągiem znaków zawierającym same spacje.

     .. note::

        By łatwo sprawdzić czy ciąg znaków zwiera same spacje, można uzyć funkcji
        ``strip``, np. ``"foo".strip()``, która zwraca ciąg znaków z którego
        "obdarto" białe znaki z lewej i prawej strony.

2. Tutaj zapytanie powinno zwracać status ``200``.

**Na 5.0**

1. Pod każdym postem pojawia się link do jego edycji, wskazujący na pole url ``/edit``,
   link ten powinien przekazywać parametr ``post_id`` o wartości równej id danego postu.
   (przypominam id każdego modelu django jest dostępny jako atrybut ``pk``).

   By przekazać za pomocą linku (czyli zapytania GET) parametry zapytania należy
   stworzyć link w postaci urlencoded czyli: ``adres?<lista parametrów>``, np.
   ``adres?foo=5&bar=6``. Parametry rodzielane są od siebie za pomocą znaku
   ``&``, sam parametr ma postać ``nazwa=wartość``.

   .. note::

      Jest jeszcze trochę możliwych problemów --- np. z obsługą polskich znaków
      w parametrach, ale o tym później.

2. Po przejściu na adres ``/edit/?post_id=5`` powinienem dostać formularz,
   w którym w polu tekst jest już wpisana treść postu (tryb edycji)
3. Jeśli nie ma postu o danym id, strona powinna zwracać status 404.
4. Po wsyłaniu formularza powinien dany post powinien zostać zedytowany,

   .. note::

      By przekazać pole ``post_id`` z zapytania ``GET`` (wyświetlającego formularz)
      do ``POST`` który go edytuje, można użyć ukrytego pola::

        <input type="hidden" name="post_id" value="..."/>


**Challenge**

Dodać do postów komentarze.

2. Komentarze są widoczne w widoku komentarzy (kolejny link pod postem)
3. Widok zawiera treść postu oraz komentarze
4. W widoku tym można też dodać komentarz




