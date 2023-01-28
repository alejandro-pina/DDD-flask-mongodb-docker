from dataclasses import dataclass


@dataclass
class UpdateUserDTO:
    id      : str
    name    : str
    email   : int
    password: int
