"""Importer for Posts"""

from datetime import datetime
from google.appengine.ext import ndb

from blog.models import Post
from importers.base import Importer


class PostImporter(Importer):
  """Importer for Posts."""

  def process(self):
    self.log("Starting to process key: " + self.key)
    data = self._getData()
    post = self._getExistingPost()

    if not post:
      self.log("Post has not been seen before, creating new one.")
      post = Post()
      post.date_published = self._getPublishedDate()
      post.key = ndb.Key("Post", self.subkey)
      post.slug = data.get('slug', self.slug)
      post.published = True
    else:
      self.log("Post has been seen before, updating existing one.")

    # As a precaution, if the post has a status that is draft, ignore it.
    if data.get('status'):
      if data['status'] == "draft":
        self.log("Caught post in Draft mode, ending processing.")
        return

    post.title = data['title']
    post.body = data.content
    post.put()

    return post.body

  def _getPublishedDate(self):
    # This creates a date to be used at this Post's published date. It's
    # imprecise and just uses the date in the slug and the current time.
    # TODO I could use a regex here but doing the simplest thing for now.
    pieces = map(int, self.subkey.split("-")[:3])
    return datetime.now().replace(year=pieces[0],
                                  month=pieces[1], day=pieces[2])

  def _getExistingPost(self):
    return Post.get_by_id(self.subkey)
