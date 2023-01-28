from dataclasses import dataclass


@dataclass
class OrderByVO:
  value: str


@dataclass(frozen=True)
class OrderByVO:
    value: str

    def __post_init__(self) -> None:
      if (not self.value) or (not "desc" in self.value and not "asc" in self.value):
        raise ValueError('Error VO: OrderByVOs - Wrong format.')

    def __str__(self) -> str:
        return self.value
