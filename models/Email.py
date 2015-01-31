import re
from peewee import *

from Utils import logger
from SenderMetadata import SenderMetadata
from flask_peewee.rest import RestAPI, RestResource
from flask import Flask
app = Flask(__name__)


db = SqliteDatabase('emails.db')

class Email(Model):
  message_id = CharField(null=True, default=None)
  message_labels = TextField(null=True, default=None)
  message_to = TextField(null=True, default=None)
  message_from = TextField(null=True, default=None)
  message_subject = TextField(null=True, default=None)
  message_date = DateField(null=True, default=None)
  serialized_json = TextField(null=True, default=None)
  sender = ForeignKeyField(SenderMetadata, null=True, default=None)
  text = TextField(null=True, default=None)

  class Meta:
    database = db

  @classmethod
  def create(cls, **query):
    inst = cls(**query)
    inst.save(force_insert=True)
    inst._prepare_instance()
    logger.info("Created Email %s", inst.message_id)
    return inst

  def _prepare_instance(self):
      self._dirty.clear()
      self.prepared()

  def prepared(self):
      pass

  def __str__(self):
    return "Message: %s\nTo: %s\nFrom: %s\nSender: %s" % (self.message_id, self.message_to, self.message_from, str(self.sender))

  def get_sender_name(self):
    match = re.search(r'(.*) <(.*)>', self.message_from)
    if match:
      return match.group(2).replace('"','')
    else:
      return None

  def get_sender_email(self):
    match = re.match(r'(.*) <(.*)>', self.message_from)
    if match:
      return match.group(2)

    match = re.match(r'[^\s<>]*@[^\s<>]*', self.message_from)
    return match.group(0)

  def politicalnewsbot_link(self):
    return "https://mail.google.com/mail/u/2/#inbox/%s?authuser=politicalnewsbotnewyork@gmail.com" % self.message_id

  def politicalnewsbotnewyork_link(self):
    return "https://mail.google.com/mail/u/inbox/%s?authuser=politicalnewsbotnewyork@gmail.com" % self.message_id

  @classmethod
  def unique_email_addresses(cls):
    return {x.email() for x in cls.select()}

@app.route('/')
def hello_world():
    return 'Hello World!'

api = RestAPI(app)

class UserResource(RestResource):
  exclude = ('sender', 'message_id', 'serialized_json', 'id', 'message_labels')

  def get_request_metadata(self, paginated_query):
        metadata = super()
        metadata.total = Email.select().count
        return metadata


# register our models so they are exposed via /api/<model>/
api.register(Email, UserResource)

# configure the urls
api.setup()

if __name__ == '__main__':
    app.run()
