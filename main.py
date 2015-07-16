#!/usr/bin/env python

import jinja2
import os
import webapp2
from os.path import join

from importers import parse_path
from blog.models import Post

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(join(os.path.dirname(__file__), "templates")),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)


class HomepageHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('index.html')

    context = {
      "posts": Post.getLatest()
    }

    self.response.write(template.render(context))


class UpdateHandler(webapp2.RequestHandler):
  def get(self):
    parse_path("posts/2014-01-20-how-i-work-coding/how-i-work-coding.md").process()
    parse_path("posts/2014-01-02-es6-arrow-functions/es6-arrow-functions.md").process()
    parse_path("posts/2014-01-12-annual-goals/annual-goals.md").process()


app = webapp2.WSGIApplication([
  ('/', HomepageHandler),
  ('/_hooks/update', UpdateHandler)
], debug=True)
