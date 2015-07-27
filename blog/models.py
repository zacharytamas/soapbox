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
  published = ndb.BooleanProperty(default=True, indexed=True)
  frontmatter = ndb.JsonProperty()

  @classmethod
  def getLatest(cls, count=5):
    return (Post.query(Post.published == True)
                .order(-Post.date_published)
                .fetch(limit=count))

  @classmethod
  def getAll(cls):
    return (Post.query(Post.published == True)
                .order(-Post.date_published)
                .fetch())
