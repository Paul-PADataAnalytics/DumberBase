from storage.storage_abc import StorageEngine
from storage.storage_router import StorageRouter


class DumberBase:
    _databases: []
    _storage_router: StorageRouter

    def __init__(self):
        self._storage_router = StorageRouter()

    def databases(self) -> list:
        return self._databases

    def open_database(self, database_path: str):
        engine = self._storage_router.identify_engine(database_path)
        return Database(database_path, engine)


class Database(object):
    _path: str
    _tables: []
    _storage_engine: StorageEngine

    def __init__(self, database_path: str, engine: StorageEngine) -> None:
        self._storage_engine = engine(database_path)
        self._path = database_path
        self._tables = self._storage_engine.get_tables()


class Table(object):
    _database: Database

    def __init__(self, Database) -> None:
        """the table creation code, tables are abstractions around the storage
        engine so this object interacts heavily with it's databases engine.

        All index and filtering code resides here.

        Arguments:
            Database -- The database that holds this table
        """
        self._database = Database

    # TODO: Add abstract here to support indexes and filtering.
