import base64

import os

import pickle
from django.db import models

# Create your models here.

class Session(models.Model):

  session_key = models.CharField(
    default=base64.b64encode(os.urandom(64)),
  )

  db_session = models.BinaryField()

  @property
  def session(self):
    return pickle.loads(bytes(self.db_session))

  @session.setter
  def session(self, val):
    self.db_session = pickle.dumps(val)