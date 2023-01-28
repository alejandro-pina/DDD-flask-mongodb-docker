from uuid import UUID
from dataclasses import dataclass


@dataclass
class UuidVO:
    value: str


@dataclass(frozen=True)
class UuidVO:
    value: str

    def __post_init__(self) -> None:
        try:
            UUID(str(self.value))
        except:
            raise ValueError('Error VO: UuidVO - Incorrect UUID.')

    def __str__(self) -> str:
        return str(self.value)
