from dataclasses import dataclass


@dataclass
class SortByVO:
    value: str

    def __post_init__(self) -> None:

        if self.value and len(self.value) > 50:
          raise ValueError('Error VO: SortByVO - Wrong format.')

        if self.value is None:
          self.value = 'registration_date'

    def __str__(self) -> str:
        return self.value
