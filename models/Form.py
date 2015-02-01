import re
from blessings import Terminal
from peewee import *

from Utils import logger
from Utils import get_answer

t = Terminal()
db = SqliteDatabase('emails.db')

class Form(Model):

  class Meta:
    database = db

  @classmethod

  def __str__(self):
    return "Form #%d" % id
