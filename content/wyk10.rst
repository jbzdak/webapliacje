Wdrażanie aplikacji Django
==========================

:date: 2016-01-11
:tags: zaj10, wykład, materiały
:category: materiały


.. note::

  Wykład do pobrania również w wersji PDF.

  .. raw:: html

     <a href="downloads/pdfs/wyk10.pdf">Wersja pdf tutaj</a>


Prezentacja pt. `Co musicie wiedzieć w biznesie <http://slides.com/jbzdak/pro-programmer#/http://slides.com/jbzdak/pro-programmer>`__

System operacyjny/założenia co do systemu
-----------------------------------------

Zakładam, że wdrażacie **małą** aplikację Django na jednej wirtualnej maszynie.

.. note::

  Biorąc pod uwagę, że największe maszyny do wynajęcia "na godzinę"
  mają ponad 30 procesorów, jest szansa, że na tego typu wdrożeniu
  możecie rozwinąć nawet spory biznes.

.. note::

  Podany pomysł na deployment ma następujące cechy:

  * Jest relatywnie prosty;
  * Jest relatywnie profesjonalny;
  * Nie jest rozwiązaniem jeśli Wasz system będzie bardzo złożony.

By hostować aplikację Django potrzebujecie bardziej zaawansowany
hosting, niż do aplikacji PHP, typowe "hostingi" z reguły nie umożliwiają
aplikacji w Pythonie w sensowny sposób.

Takie maszyny wirtualne można relatywnie tanio założyć w wielu miejscach:

* `Linode <https://www.linode.com/pricing>`__ --- miałem/mam u nich trochę 
  systemów i są stabilni i nie robią problemów;
* `Digital Ocean <https://www.digitalocean.com/>`__ --- jak wyżej (ale miałem
  mniej doświadczenia);
* `Amazon AWS <https://aws.amazon.com/>`__ --- bardzo stabilne, mniej łatwe
  w korzystaniu;

.. note::

  Decyzja o wybraniu systemu hostingowego jest dość ważna, więc to, że jedna
  osoba powiedziała Wam, że jakiś system hostingowy jest OK **nie jest**
  dostatecznie dobrą rekomendacją.

Zakładam, że macie tam zainstalowanego najnowszego stabilnego Debiana (Jessie).

Co potrzebne jest do wdrożenia aplikacji Django
-----------------------------------------------

Serwer HTTP
  Serwer HTTP powinien być pierwszym punktem kontaktu użytkownika z systemem.

  Może on pełnić takie funkcje:

  * Wykonywać obsługę SSL;
  * Dokonywać kompresji/dekompresji zapytań i odpowiedzi (jest to
    funkcjonalność HTTP);
  * Serwowanie statycznych plików;
  * Filtrować zapytania, które wykonują znane ataki (tego nie ma w materiale).

  Wszystkie te rzeczy może robić kod Pythona, ale wydajniej jest przerzucić 
  te odpowiedzialności na bardzo wydajny i napisany w C server.

  Dodatkowo pełni on dość ważną rolę --- buforuje zapytanie, tj.
  zapytanie użytkownika jest trzymane w pamięci,
  i przekazywane do aplikacji dopiero, gdy zostanie przesłane w całości.

  Przyśpiesza to cały system, ponieważ aplikacja nie czeka na dane od
  użytkownika, dodatkowo chroni przed `atakiem slowloris <https://en.wikipedia.org/w/index.php?title=Slowloris_%28software%29&oldid=683765857>`__


Kontener aplikacji
  odpowiada on za przekazanie zapytania do wątka
  przetwarzającego oraz zarządza wątki/procesy przetwrzające.

  Tę rolę będzie pełnił uWSGI.

Aplikację
  Wasza aplikacja też musi być na serwerze

Serwer bazodanowy
  Myślę że nie wymaga opisu

Konfiguracja Systemu operacyjnego
---------------------------------

Każda usługa powinna mieć swojego użytkownika. Naszego nazwijmy ``webapp``.
Należy go stworzyć.

Instalujemy wymagane oprogramowanie:

* Bazę danych ``postgresql``
* Serwer ``nginx``

Kompilacja Pythona
------------------

Instalujemy Paczki konieczne do kompilacji pythona ``aptitude build-dep --without-recommends python3.X``,
gdzie X jest najnowszym dostępnym Pythonem.

Pobieramy pythona i kompilujemy go np. do ``/opt/python3.5``.

.. note::

  Pythona kompilujemy, by mieć własny interpreter niezależny od systemowego,
  systemowy może się odświerzyć na nowszy, który będzie niekompatybilny
  z kodem z wirtualnego środowiska.

  Jeśli macie więcej niż kilka serwerów, lepszym pomysłem jest stworzenie
  paczki z "Waszym" pythonem.

Konfiguracja bazy danych
------------------------

Stwórzcie bazę danych o nazwie np. ``webapp`` i dajcie do niej uprawnienia
użytkownikowi ``webapp``.

W postgresql (na debiane) ::

  sudo -u postgres bash -c 'createuser webapp && createdb webapp webapp'

``sudo -u postgres``

  Przelogowujemy się na użytkownika postgresql, który zarządza bazą danych.

``createuser webapp``

  Tworzy bazodanowego użytkownika ``webapp``

``createdb A B``

  Tworzy bazę danych o nazwie ``A`` z właścicielem ``B``.

Konfiguracja webaplikacji
-------------------------

Tworzycie wirtualne środowisko w ``/home/webapp/venv`` i instalujecie do niego
potrzebne paczki.

Pobieracie aplikacje do katalogu ``/home/webapp/repo``.

Tworzycie plik ``prod_settings.py`` który zawiera konfigurację serwera
produkcyjnego. Umieszczacie go ``/home/webapp/repo``.

Jeśli wszystko dobrze zrobiliście możecie sprawdzić czy działa poprzez::

  ``/home/webapp/venv/bin/python /home/webapp/repo/manage.py --settings prod_settings runserver``

Uruchomi to developerski server django, jeśli możecie się do niego polączyć
wszystko jest OK.

.. note::

  By uruchomić Django musicie powiedzieć mu jaki plik settings musi załadować.

  W tym celu służy argument ``--settings prod_settings``, albo zmienna
  systemowa ``DJANGO_SETTINGS_MODULE``.

Konfiguracja uwsgi
------------------

Uwsgi jest kontenerem aplikacji i jest **bardzo fajny**. Zainstalujcie go w
wirtualnym środowisku:: ``/home/webapp/venv/bin/pip install uwsgi``.

Uwsgi można konfigurować za pomocą pliku ``.ini``, swórzcie plik
``/home/webapp/uwsgi.ini`` o treści::

   module=webapp.wsgi
   pythonpath=/home/webapp/repo
   http=8000

Instrukcja ``webapp.wsgi`` musi wskazywać na moduł (plik Pythona) o nazwie
``wsgi.py`` wygenerowany przez django, może on u Was być np. w katalogu
``/home/webapp/repo/superapka/wsgi.py`` wtedy należy napisać
``module=superapka.wsgi``.

Jeśli napiszecie ``DJANGO_SETTINGS_MODULE=prod_settings /home/webapp/venv/bin/uwsgi --ini /home/webapp/uwsgi.ini``
serwer uwsgi powinien się uruchomić (można to sprawdzić wchodząc na localhost:8000).

Teraz podmieńcie ``uwsgi.ini`` na:

   module=webapp.wsgi
   pythonpath=/home/webapp/repo
   socket=8000

.. note::

  Pozwoli to użyć protokołu uwsgi, który przyśpieszy komunikację.


Uruchamianie uwsgi za pomocą systemd
------------------------------------

Usługi systemowe w nowszych linuksach uruchamiane są za pomocą ``systemd``,
by stworzyć taką usługę należy napisać plik o takiej zawartości::


    [Unit]
    Description=Description
    After=syslog.target

    [Install]
    WantedBy=multi-user.target

    [Service]
    # What process to start
    ExecStart=/home/webapp/venv/bin/uwsgi --ini /home/webapp/uwsgi.ini
    # What user log to
    User=webapp
    # Working directory
    ENVIORMENT="DJANGO_SETTINGS_MODULE=prod_settings"
    WorkingDirectory=/home/webapp/repo
    Restart=always
    # Kill by SIGQUIT signal --- this is what asks wsgi to die nicely
    KillSignal=SIGQUIT
    # Notify type, in this type uwsgi will inform systemd that it is ready to handle requests
    Type=notify
    StandardError=syslog
    NotifyAccess=all

i umieścić go w ``/etc/systemd/system/webapp.service``. Następnie włączyć ową usługę::

    sudo systemctl --system enable webapp
    sudo systemctl start webapp

Od teraz Wasz ``uwsgi`` powinno urchamiać się samo.

Konfiguracja ``nginx``
----------------------

Podsawowa konfiuracja nginxa::

    upstream django {
        # Konfiguruje serwer, do którego nginx przekazuje połączenia
        server 127.0.0.1:8000; # for a web port socket (we'll use this first)
    }

    # configuration of the server
    server {
        # the port your site will be served on
        listen      80 default_server;
        # the domain name it will serve for
        server_name .example.com; # substitute your machine's IP address or FQDN
        charset     utf-8;

        # Maksymalny rozmiar przychodzącego zapyania
        # np. maksymalny rozmiar załączonego pliku
        client_max_body_size 75M;   # adjust to taste

        # Przekierowanie wszystkich zapytań do django
        location / {
            uwsgi_pass  django;
            include     /etc/nginx/uwsgi_params; # the uwsgi_params file you installed
        }
    }

Konfigruacja statycznych plików
-------------------------------

Django, w konfiguracji produkcyjnej, nie wysyła statycznych plików. Musi to
robić nginx. By to zrobić należy:

* Stworzyć katalog: ``/home/webapp/static``
* Powiedzieć Django, że pliki statyczne są mają być składowane w katalogu:
  ``/home/webapp/static``.  By to zrobić należy dodać do pliku settings
  opcję: ``STATIC_ROOT = '/home/webapp/static'``.
* Wykonać komendę kopiującą pliki: ``manage.py collectstatic``.
* Skonfigurować nginxa do serwowania statycznych plików, w tym celu
  należy dodać do niego sekcję::

    location /static {
        alias /home/webapp/static;
    }

  sekcja ta powinna być **przed** sekcją ``location /``.




















