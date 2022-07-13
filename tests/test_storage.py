import pytest

from tests.resources.test_storage_engine import TestStorageEngine


@pytest.fixture
def dummy_engine() -> TestStorageEngine:
    return TestStorageEngine()


def test_create_database(dummy_engine):
    dummy_engine.create_database(database_path="/test/path/for/testing")
    assert "/test/path/for/testing" in dummy_engine.databases
