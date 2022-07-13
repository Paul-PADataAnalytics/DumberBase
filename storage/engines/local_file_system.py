# from os import path
from storage.storage_abc import StorageEngine


class LocalFileSystem(StorageEngine):

    database_name: str
    database_path: str

    def create_database(self, database_path):
        pass

    def delete_database(self, database_path):
        pass

    def create_table(self, database_path):
        pass

    def delete_table(self, database_path):
        pass

    def read_record(self, table_path):
        pass

    def write_record(self, table_path, content):
        pass
