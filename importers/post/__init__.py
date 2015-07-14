"""Importer for Posts"""

from datetime import datetime
from google.appengine.ext import ndb

from models.post import Post
from importers.base import Importer


class PostImporter(Importer):
  """Importer for Posts."""

  def process(self):
    data = self._getData()
    post = self._getExistingPost()

    if not post:
      post = Post()
      post.date_published = self._getPublishedDate()

    # As a precaution, if the post has a status that is draft, ignore it.
    if data.get('status'):
      if data['status'] == "draft":
        return

    post.title = data['title']
    post.body = data.content
    post.key = ndb.Key("Post", self.subkey)
    post.slug = data.get('slug', self.slug)

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
