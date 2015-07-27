
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

    self.render_to_response('blog/post-detail.html', {
      'post': post
    })


class PostsIndexHandler(BlogHandler):

  def get(self):
    # TODO This page should be basically entirely cached since it will grow to
    # be increasingly less performant as I post more.
    posts = Post.getAll()

    if not posts:
      # TODO This shouldn't actually happen because I will always have
      # at least one Post.
      pass

    self.render_to_response('blog/post-index.html', {
      "posts": posts
    })
