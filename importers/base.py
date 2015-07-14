
from google.appengine.api import urlfetch
import frontmatter
import logging

BASE_URI = "https://raw.githubusercontent.com/zacharytamas/web-data/master/"


class Importer(object):

  key = None
  subkey = None
  slug = None

  def __init__(self, key):
    self.key = key
    self.subkey = key.split("/")[1]
    self.slug = self._getSlug(key)

  def log(self, s):
    logging.info("I/%s : %s" % (self.__class__.__name__, s))

  def _getSlug(self, key):
    return key.split("/")[2].replace(".md", "")

  def _getData(self):
    result = urlfetch.fetch(BASE_URI + self.key)

    if result.status_code == 200:
      return frontmatter.loads(result.content)
    else:  # TODO handle other cases
      pass
