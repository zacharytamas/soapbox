from google.appengine.ext import ndb


class Post(ndb.Model):
  """A blog post on my website."""
  date_first = ndb.DateTimeProperty(auto_now_add=True)
  date_published = ndb.DateTimeProperty()
  date_updated = ndb.DateTimeProperty(auto_now=True)
  title = ndb.StringProperty()
  body = ndb.TextProperty()
  slug = ndb.StringProperty(indexed=True)
  tags = ndb.StringProperty(repeated=True)
