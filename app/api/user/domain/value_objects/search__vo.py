from dataclasses import dataclass


@dataclass
class SearchVO:
  value: str


@dataclass(frozen=True)
class SearchVO:
    value: str

    def __post_init__(self) -> None:
        if len(self.value) > 50:
            raise ValueError('Error VO: SearchVO - Excecive word in search.')

    def __str__(self) -> str:
        return self.value
