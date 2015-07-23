
import jinja2
import os
import webapp2
from os.path import join

from models import Post

# TODO Extract this into one shared environment for the whole site.
# This is a copy-paste job for rapid iteration.
JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(join(os.path.dirname(__file__), "../templates")),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)


class BlogHandler(webapp2.RequestHandler):
  pass


class PostDetailHandler(BlogHandler):

  def get(self, post_slug):
    post = Post.query(Post.slug == post_slug).get()

    if not post:
      # TODO Throw a 404.
      pass

    template = JINJA_ENVIRONMENT.get_template('blog/post-detail.html')

    context = {
      'post': post
    }

    self.response.write(template.render(context))
