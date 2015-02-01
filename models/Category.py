import re
from blessings import Terminal
from peewee import *

from Utils import logger
from Utils import get_answer

from Form import Form

t = Terminal()
db = SqliteDatabase('emails.db')

class Category(Model):
  name = CharField(null=True, default=None)

  class Meta:
    database = db

  @classmethod

  def __str__(self):
    return self.email_address + " (%s)" % self.comment
