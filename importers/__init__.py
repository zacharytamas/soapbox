
from post import PostImporter


def parse_path(path):
  """Accepts a path and returns an instance of an Importer needed for it."""

  path_key = path.split("/")[0]

  if path_key == "posts":
    return PostImporter(path)
