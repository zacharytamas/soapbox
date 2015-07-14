#!/usr/bin/env python

import webapp2

from importers import parse_path


class MainHandler(webapp2.RequestHandler):
  def get(self):
    importer = parse_path("posts/2014-01-12-annual-goals/annual-goals.md")
    self.response.write(importer.process())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
