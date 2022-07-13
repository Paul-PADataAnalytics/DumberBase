from storage.storage_abc import StorageEngine


class TestStorageEngine(StorageEngine):

    database_path: str
    databases: list
    tables: list

    def __init__(self, database_path: str):
        self.database_path = database_path
        self.databases = []
        self.tables = []

    def create_database(self, database_path):
        self.databases.append(database_path)

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

    def get_tables(self):
        pass
