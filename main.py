#!/usr/bin/env python

import webapp2
from webapp2_extras import routes

from importers import parse_path
from utils import render_to_text
from blog.models import Post

from blog.routes import routes as blog_routes
from pages.handlers import PageHandlerFactory


class HomepageHandler(webapp2.RequestHandler):
  def get(self):

    context = {
      "posts": Post.getLatest()
    }

    self.response.write(render_to_text('index.html', context))


class UpdateHandler(webapp2.RequestHandler):
  def get(self):
    posts = [
      "posts/2014-01-20-how-i-work-coding/how-i-work-coding.md",
      "posts/2014-01-02-es6-arrow-functions/es6-arrow-functions.md",
      "posts/2014-01-12-annual-goals/annual-goals.md",

      "pages/about.md"
    ]

    for key in posts:
      parse_path(key).process()


app = webapp2.WSGIApplication([
  ('/', HomepageHandler),
  ('/about/', PageHandlerFactory.HandlerFor('about')),

  routes.PathPrefixRoute('/posts', blog_routes),

  ('/_hooks/update', UpdateHandler)
], debug=True)
