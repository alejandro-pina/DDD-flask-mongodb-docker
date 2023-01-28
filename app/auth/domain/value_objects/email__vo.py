import re
from dataclasses import dataclass
from email.utils import parseaddr

EMAIL_REGEX = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"


@dataclass
class EmailVO:
  value: str


@dataclass(frozen=True)
class EmailVO:
    value: str

    def __post_init__(self) -> None:
        real_name, email_address = parseaddr(self.value)

        if not real_name and not email_address:
            raise ValueError('Error VO: EmailVO - Incorrect email address.')

        regex_result = re.search(
            EMAIL_REGEX,
            email_address,
        )
        if not regex_result:
            raise ValueError('Error VO: EmailVO - Incorrect email address.')

    def __str__(self) -> str:
        return self.value
