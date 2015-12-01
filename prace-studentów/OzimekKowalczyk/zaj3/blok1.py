# -*- coding: utf-8 -*-
import unittest, math


def zad1():
  """
  Proszę do ciała tej funkcji wpisać kod który policzy sumę liczb całkowitych
  z zakresu 0..100, za pomocą funkcji for.

  Test:

  >>> zad1() == 5050
  True
  >>> "for" in helper_getsource(zad1)
  True
  """
  n=101
  sum=0
  for i in range(1,n):
    sum=sum+i
  return sum

def zad2():
  """
  Proszę w ciele tej funkcji wyznaczyć wartość całki z sinusa na zakresie od
  zera do dwa pi korzystając z 1E5 przedziałów załkowania.
  """
  start = 0
  end = math.pi*2
  for i in range(1000001):
    s=0.0
    delta=float(end-start)/100000.0
    g=i*delta
    h=(i+1.0)*delta
    y_i=float(sin(start+g))
    y_ii=float(sin(start+h))
    s +=1.0/2.0*(y_i+y_ii)*delta

  return s


def zad3_arange(start, stop, step):
 n=int(round((stop-start)/float(step)))
 if n > 1:
  return([round(start+step*i,2) for i in range(n+1)])
 else:
  return([])

ZAD3_DATA  = [
    {"imie":"Kociorro","age":5,"kolor oczu":"niebieskie"},
    {"imie":"Hrabia","age":6,"kolor oczu":"czarne"},
    {"imie":"Królewicz","age":2,"kolor oczu":"zielone"},
    {"imie":"Mruchuś","age":1,"kolor oczu":"błękitne"},
    {"imie":"Bonifacy","age":10,"kolor oczu":"niebieskie"}
]
"""
Podmień definicję zmiennej DATA tak by:

Była to lista słowników, każdy słownik reprezentuje jedno zwierze.
Lista powinna mieć 5 elementów, a każde zwierze przynajmniej atrybuty
3 w tym imię.

Do pobrania imienia trzeciego zwierzęcia powinno mi starczyć 
wywołania data[2]['imie'].
"""



#### TESTY

class TestBlok1Zaj1(unittest.TestCase):

  def test_result(self):
    self.assertEqual(zad1(), 5050)

  def test_for(self):
    self.assertIn("for", helper_getsource(zad1))

class TestBlok1Zaj2(unittest.TestCase):

  def test_result(self):
    self.assertAlmostEqual(zad2(), 0)

  def test_sin(self):
    self.assertIn("sin", helper_getsource(zad2))

  def test_for(self):
    self.assertIn("for", helper_getsource(zad2))


class TestBlok1Zaj3(unittest.TestCase):

  def test_result_type(self):
    self.assertIsInstance(zad3_arange(1, 2, 3), list)

  def test_result(self):
    self.assertEqual(zad3_arange(1, 2, 3), [1])

  def test_result_2(self):
    expected = [1, 1.3, 1.6, 1.9]
    result = zad3_arange(1, 2, .3)
    for ii, (left, right) in enumerate(zip(expected, result)):
      with self.subTest("Element {}".format(ii)):
        self.assertAlmostEqual(left,right)

class TestBlok1Zad4(unittest.TestCase):

  def test_result_type(self):
    self.assertIsInstance(ZAD3_DATA, list)

  def test_contents_type(self):
    for e in ZAD3_DATA:
      self.assertIsInstance(e, dict)

  def test_keys(self):
    for e in ZAD3_DATA:
      self.assertIn('imie', e)

  def test_len(self):
    self.assertEqual(5, len(ZAD3_DATA))


def helper_getsource(func):
  import inspect, re
  lines = []
  var = 0
  for line in inspect.getsourcelines(func)[0][1:]:
    if var >= 2:
      lines.append(line)
    if '''"""''' in line:
      var+=1
  code = "\n".join(lines)
  return re.sub('"""(^["])+"""', '', code, flags=re.MULTILINE)
