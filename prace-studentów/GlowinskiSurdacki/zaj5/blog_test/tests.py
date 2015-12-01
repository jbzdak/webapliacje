import datetime
from django.core.exceptions import ImproperlyConfigured, FieldDoesNotExist
from django.test import TestCase, Client


# Create your tests here.

def get_blogpost_model():
  from django.apps import apps
  try:
    blog_app = apps.get_app_config("blog_app_solution")
  except LookupError:
    try:
      blog_app = apps.get_app_config("blog_app")
    except LookupError:
      raise AssertionError("Nie ma aplikacji 'blog_app'")

  try:
    return blog_app.get_model("BlogPost")
  except LookupError:
    raise AssertionError("Nie ma modelu BlogPost w aplikacji blog_app")

class TestFor3Base(TestCase):

  def test_models_are_installed(self):
    get_blogpost_model()

  def test_model_fields(self):
    model = get_blogpost_model()

    try:
      model._meta.get_field('text')
    except FieldDoesNotExist:
      self.fail("Nie ma pola text")

    try:
      model._meta.get_field('posted_at')
    except FieldDoesNotExist:
      self.fail("Nie ma pola posted_at")

class TestFor3(TestCase):

  def setUp(self):
    self.BlogPost = get_blogpost_model()

  def test_for_empty_list(self):
    c = Client()
    response = c.get("/index/")
    self.assertIn('No posts to show', response.content.decode("utf-8"))

  def test_entries_are_displayed(self):
    self.BlogPost.objects.create(text="foo")
    self.BlogPost.objects.create(text="bar")
    c = Client()
    response = c.get("/index/")
    self.assertNotIn('No posts to show', response.content.decode("utf-8"))
    self.assertIn('foo', response.content.decode("utf-8"))
    self.assertIn('bar', response.content.decode("utf-8"))

  def test_ordering(self):
    self.BlogPost.objects.create(text="foo", posted_at=datetime.datetime(1985, 9, 19, 18, 30))
    self.BlogPost.objects.create(text="bar", posted_at=datetime.datetime(1985, 9, 19, 19, 30))
    c = Client()
    response = c.get("/index/")
    c = response.content.decode("utf-8")
    self.assertNotIn('No posts to show', c, "Jeśli są posty do pokazania to napis 'no posts to show' nie powinien się pojawiać" )
    self.assertIn('foo', c, "Treści postów powinny pojawiać się na stronie")
    self.assertIn('bar', c, "Treści postów powinny pojawiać się na stronie")

    self.assertLess(c.index('bar'), c.index('foo'), "Starszy post powinien pojawiać się pod młodszym")

  def test_add(self):
    self.assertEqual(self.BlogPost.objects.count(), 0)
    response = self.client.post("/edit/", {"text":"foo"})
    self.assertEqual(response.status_code, 302, "Widok /edit/ powinien zwrócić przekierowanie przy udanym dodaniu postu")
    self.assertEqual(self.BlogPost.objects.count(), 1, "Po wykonaniu /edit/ powinien w bazie danych pojawić się blog post")
    bp = self.BlogPost.objects.all()[0]
    self.assertEqual(bp.text, 'foo')
    self.assertIsNotNone(bp.posted_at)


class TestFor4(TestCase):

  def test_error_when_no_text(self):
    response = self.client.post("/edit/", {})
    self.assertEqual(response.status_code, 200, "Przy braku tekstu strona powinna zwracać status 200")
    self.assertIn('Please add post text', response.content.decode("utf-8"))


  def test_error_when_no_empty(self):
    response = self.client.post("/edit/", {'text': ''})
    self.assertEqual(response.status_code, 200, "Przy braku tekstu strona powinna zwracać status 200")
    self.assertIn('Please add post text', response.content.decode("utf-8"))


  def test_error_when_whitespace(self):
    response = self.client.post("/edit/", {'text': ' \n\t\r'})
    self.assertEqual(response.status_code, 200, "Przy braku tekstu strona powinna zwracać status 200")
    self.assertIn('Please add post text', response.content.decode("utf-8"))

class TestsFor5(TestCase):

   def test_error_when_no_text(self):
    response = self.client.post("/edit/", {})
    self.assertEqual(response.status_code, 200, "Przy braku tekstu strona powinna zwracać status 200")
    self.assertIn('Please add post text', response.content.decode("utf-8"))

