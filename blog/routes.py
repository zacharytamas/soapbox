
import webapp2

from .handlers import PostDetailHandler
from .handlers import PostsIndexHandler

routes = [
  webapp2.Route('/', handler=PostsIndexHandler),
  webapp2.Route('/<post_slug:[\w\-]+>/', handler=PostDetailHandler)
]
