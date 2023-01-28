from dataclasses import dataclass


@dataclass
class NameVO:
  value: str


@dataclass(frozen=True)
class NameVO:
    value: str

    def __str__(self) -> str:
        return self.value
