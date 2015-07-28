
import jinja2
import os
from os.path import join
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(join(os.path.dirname(__file__), "templates")),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)


def _date(value, format='%d-%m-%Y'):
  return value.strftime(format)

JINJA_ENVIRONMENT.filters['date'] = _date


################################################################
# Convenience methods
################################################################


def get_template(template_name):
  return JINJA_ENVIRONMENT.get_template(template_name)


def render_to_text(template_name, context):
  return get_template(template_name).render(context)


class BaseHandler(webapp2.RequestHandler):
  def render_to_response(self, template_name, context):
    self.response.write(render_to_text(template_name, context))
