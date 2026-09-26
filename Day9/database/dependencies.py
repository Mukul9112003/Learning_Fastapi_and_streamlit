from collections.abc import Generator

from config.settings import settings

from database.base import Database
from database.factory import DatabaseFactory


def get_database() -> Generator[Database, None, None]:

    database = DatabaseFactory.create(
        settings.database_type
    )

    yield database