
import webapp2

from utils import render_to_text

from .models import Post


class BlogHandler(webapp2.RequestHandler):
  def render_to_response(self, template_name, context):
    self.response.write(render_to_text(template_name, context))


class PostDetailHandler(BlogHandler):

  def get(self, post_slug):
    post = Post.query(Post.slug == post_slug).get()

    if not post:
      # TODO Throw a 404.
      pass

    context = {
      'post': post
    }

    self.render_to_response('blog/post-detail.html', context)
