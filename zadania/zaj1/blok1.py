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
  return

def zad2():
  """
  Proszę w ciele tej funkcji wyznaczyć wartość całki z sinusa na zakresie od
  zera do dwa pi korzystając z 1E5 przedziałów załkowania.
  """
  start = 0
  end = math.pi*2
  return math.sin(0)


def zad3_arange(start, stop, step):
  """
  Napisz funkcję która jest lepszą wersją funkcji range, funkcja ta dziala również
  dla liczb zmiennoprzecinkowych.

  Powinna ona przyjmować trzy argumenty:

  * start --- początek iteracji
  * stop --- koniec iteracji
  * step --- krok iteracji

  i zwracać listę która zawiera wszystkie liczby w postaci start + i*step
  mniejsze od stop.

  Np. zad3_arange(0, 5, 1) zwraca: [0, 1, 2, 3, 4]
  zad3_arange(0, 5, .1) zwraca: [0, .1, .2 ..., 3, ... 4.9]
  """
  return None

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
    self.assertIn("sin(", helper_getsource(zad2))

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


if __name__ == '__main__':

  print(helper_getsource(zad1))