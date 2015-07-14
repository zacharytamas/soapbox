#!/usr/bin/env python

import jinja2
import os
import webapp2

from importers import parse_path
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
  def get(self):
    importer = parse_path("posts/2014-01-12-annual-goals/annual-goals.md")
    self.response.write(importer.process())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
