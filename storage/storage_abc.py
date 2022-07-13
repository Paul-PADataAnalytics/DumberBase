from abc import ABC, abstractmethod


class StorageEngine(ABC):
    """Abstract class that embodies the requirements of storing and
    retrieving data.  Inherit this class and implement all the
    abstract methods and properties found herein.

    Arguments:
        ABC -- The abstract class master object

    Raises:
        NotImplementedError: Raised when a key method is not implemented
    """

    @abstractmethod
    def __init__(self, database_path: str) -> None:
        """Connect to the database, where ever it is and pull all the
        necessary details.

        Arguments:
            database_path -- path to the database as a url
        """
        pass

    @abstractmethod
    def write_record(self, table_name: str, content):
        """Write a record, or many records to a path.

        Arguments:
            table_name -- the name of the table to write to
            content -- a dict, or an iterable of dicts forming the writable
                       record
        """
        raise NotImplementedError("Write_file not implemented")

    @abstractmethod
    def read_record(self, table_name: str, id: str = None):
        """read a single record with the ID of id.

        Arguments:
            table_name -- the name of the table to read from

        Keyword Arguments:
            id -- record ID (default: {None})
        """
        raise NotImplementedError("Read_file not implemented")

    @abstractmethod
    def create_table(self, database_path: str):
        raise NotImplementedError("Create_directory not implemented")

    @abstractmethod
    def delete_table(self, database_path: str):
        raise NotImplementedError("Delete_directory not implemented")

    @abstractmethod
    def create_database(self, database_path: str):
        raise NotImplementedError("Create_database not implemented")

    @abstractmethod
    def delete_database(self, database_path: str):
        raise NotImplementedError("Delete_database not implemented")

    @abstractmethod
    def get_tables(self) -> list:
        """Returns list of tables

        Returns:
            list
        """
        raise NotImplementedError("Get_tables not implemented")
