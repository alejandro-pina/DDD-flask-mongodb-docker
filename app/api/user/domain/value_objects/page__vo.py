from dataclasses import dataclass


@dataclass
class PageVO:
  value: int


@dataclass(frozen=True)
class PageVO:
    value: int

    def __post_init__(self) -> int:
        if not isinstance(self.value, int) or self.value > 1000:
            raise ValueError('Error VO: PageVO - Page > 1000.')
        return self.value
