#!/usr/bin/env python

import jinja2
import os
import webapp2

from importers import parse_path
from models.post import Post

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
  def get(self):
    importer = parse_path("posts/2014-01-20-how-i-work-coding/how-i-work-coding.md")
    importer.process()

    posts = Post.getLatest()

    template = JINJA_ENVIRONMENT.get_template('index.html')

    context = {
      "posts": posts
    }

    self.response.write(template.render(context))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
