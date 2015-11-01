from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):

  return HttpResponse(content='Hello World')

ASK_TEMPLATE= """
  <!DOCTYPE html>
  <html xmlns="http://www.w3.org/1999/html">
  <head>
      <meta charset="utf-8">
  </head>
  <body>
    <h1>Podaj Imię<h1>
    <form action="greet" method="GET">
      <input name="name">
      <button> Submit</button>
    </form>
  </body>
  </html>
"""

def get_name(request):
  return HttpResponse(content=ASK_TEMPLATE)

def greet_by_name(request):
  return HttpResponse(content="Witaj {}!".format(request.GET['name']))