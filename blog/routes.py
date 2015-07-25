
import webapp2

from .handlers import PostDetailHandler

routes = [
  webapp2.Route('/<post_slug:[\w\-]+>/', handler=PostDetailHandler)
]
