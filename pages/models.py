from google.appengine.ext import ndb


class Page(ndb.Model):
  """A static page on my website."""
  date_first = ndb.DateTimeProperty(auto_now_add=True)
  date_published = ndb.DateTimeProperty()
  date_updated = ndb.DateTimeProperty(auto_now=True)
  title = ndb.StringProperty()
  body = ndb.TextProperty()
  slug = ndb.StringProperty(indexed=True)
  tags = ndb.StringProperty(repeated=True)
  published = ndb.BooleanProperty(default=True, indexed=True)
  frontmatter = ndb.JsonProperty()

  @classmethod
  def getBySlug(cls, slug):
    return Page.query(Page.slug == slug).get()

  @classmethod
  def getLatest(cls, count=5):
    return (Page.query(Page.published == True)
                .order(-Page.date_published)
                .fetch(limit=count))

  @classmethod
  def getAll(cls):
    return (Page.query(Page.published == True)
                .order(-Page.date_published)
                .fetch())
