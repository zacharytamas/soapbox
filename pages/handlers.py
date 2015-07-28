
from utils import BaseHandler

from .models import Page


class PageHandlerFactory(object):
  """Generate PageHandler preconfigured instances for certain pages."""

  @classmethod
  def HandlerFor(cls, slug):
    class stub(PageHandler):
      page_slug = slug
    return stub


class PageHandler(BaseHandler):
  page_slug = None

  def get(self, page_slug=None):
    if page_slug is None:
      page_slug = self.page_slug

    page = Page.getBySlug(self.page_slug)

    if not page:
      # TODO Throw a 404.
      pass

    self.render_to_response('pages/page-detail.html', {
      'page': page
    })
