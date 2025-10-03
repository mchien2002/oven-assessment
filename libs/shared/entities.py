from dataclasses import dataclass, asdict
from typing import TypeVar


@dataclass(kw_only=True)
class BaseEntity:
    def to_dict(self):
        return asdict(self)

    def serialize(self):
        return self.to_dict()


EntityType = TypeVar("EntityType", bound=BaseEntity)
