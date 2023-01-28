from dataclasses import dataclass


@dataclass
class IdxVO:
	value: int


@dataclass(frozen=True)
class IdxVO:
	value: int

	def __post_init__(self) -> int:
		if not isinstance(self.value, int) or self.value > 1000000:
			raise ValueError('Error VO: IdxVO - index > 1000000.')
		return self.value
