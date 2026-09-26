from database.base import Database


class DatabaseFactory:

    _registry = {}

    @classmethod
    def register(cls, name: str, creator):
        cls._registry[name] = creator

    @classmethod
    def create(cls, name: str) -> Database:

        creator = cls._registry.get(name)

        if creator is None:
            raise ValueError(
                f"Database '{name}' is not registered"
            )

        return creator()