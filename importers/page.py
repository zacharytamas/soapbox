"""Importer for Pages"""

import markdown
from datetime import datetime
from google.appengine.ext import ndb

from pages.models import Page
from importers.base import Importer


class PageImporter(Importer):
  """Importer for Pages."""

  def process(self):
    self.log("Starting to process key: " + self.key)
    data = self._getData()
    page = self._getExistingPage()

    if not page:
      self.log("Page has not been seen before, creating new one.")
      page = Page()
      page.date_published = self._getPublishedDate()
      page.key = ndb.Key("Page", self.subkey)
      page.slug = data.get('slug', self.slug)
      page.published = True
    else:
      self.log("Page has been seen before, updating existing one.")

    # As a precaution, if the page has a status that is draft, ignore it.
    if data.get('status'):
      if data['status'] == "draft":
        self.log("Caught page in Draft mode, ending processing.")
        return

    page.title = data['title']
    page.body = self._renderBody(data.content)
    page.frontmatter = data.to_dict()
    self._inflateStatic(data.content)
    page.put()

    return page.body

  def _renderBody(self, content):
    body = markdown.markdown(content)
    body = self._inflateStatic(body)
    return body

  def _inflateStatic(self, content):
    self.log("TODO Inflate static files")
    # TODO This will check the HTML for any relative links to static assets
    # such as images, upload them to Google Cloud, and then replace their
    # link with the public link of their copy.
    return content

  def _getPublishedDate(self):
    return datetime.now()

  def _getExistingPage(self):
    return Page.get_by_id(self.subkey)
