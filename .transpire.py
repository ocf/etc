from pathlib import Path

from transpire.types import Image

name = "etc"


def images():
    yield Image(name="sync", path=Path("/sync"))
