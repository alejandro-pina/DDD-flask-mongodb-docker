from dataclasses import dataclass


@dataclass
class FieldDateVO:
    value: str

    def __post_init__(self) -> None:

        if self.value and len(self.value) > 20:
          raise ValueError('Error VO: FieldDateVO - Wrong format.')

        if self.value is None:
          self.value = 'registration_date'

    def __str__(self) -> str:
        return self.value
