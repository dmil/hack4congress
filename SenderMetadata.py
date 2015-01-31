import re
from blessings import Terminal
from peewee import *

from Utils import logger
from Utils import get_answer

t = Terminal()
db = SqliteDatabase('emails.db')

class SenderMetadata(Model):
  email_address = CharField(null=True, default=None, unique=True)
  email_url = CharField(null=True, default=None)
  in_district = BooleanField(null=True, default=None)

  class Meta:
    database = db

  @classmethod
  def create(cls, **query):
    inst = cls(**query)
    inst.save(force_insert=True)
    inst._prepare_instance()
    return inst

  def _prepare_instance(self):
    self._dirty.clear()
    self.prepared()

  def prepared(self):
    pass

  def __str__(self):
    return self.email_url + " (%s)" % self.party
