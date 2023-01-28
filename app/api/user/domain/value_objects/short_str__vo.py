from dataclasses import dataclass


@dataclass
class ShortStrVO:
  value: str


@dataclass(frozen=True)
class ShortStrVO:
    value: str

    def __post_init__(self) -> None:
        if len(self.value) > 20:
            raise ValueError('Error VO: ShortStrVO - Max str 20 characters.')

    def __str__(self) -> str:
        return self.value
