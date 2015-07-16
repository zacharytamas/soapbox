#!/usr/bin/env python

import jinja2
import os
import webapp2

from importers import parse_path
from blog.models import Post

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
  def get(self):
    parse_path("posts/2014-01-20-how-i-work-coding/how-i-work-coding.md").process()
    parse_path("posts/2014-01-02-es6-arrow-functions/es6-arrow-functions.md").process()
    parse_path("posts/2014-01-12-annual-goals/annual-goals.md").process()

    posts = Post.getLatest()

    template = JINJA_ENVIRONMENT.get_template('index.html')

    context = {
      "posts": posts
    }

    self.response.write(template.render(context))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
