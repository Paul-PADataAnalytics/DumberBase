from urllib import parse
import storage.engines as engines
from storage.storage_abc import StorageEngine


class StorageRouter(object):
    """The storage router takes a given URL for a database path and
    returns an appropriate storage engine"""

    found_engines: dict

    def __init__(self):
        self.found_engines = {}
        self.load_engines()

    def load_engines(self):
        for engine in engines:
            if issubclass(engine, StorageEngine):
                self.found_engines[engine.scheme] = engine

    def identify_engine(self, url: str):
        return self.found_engines[parse.urlparse(url)["scheme"]]
