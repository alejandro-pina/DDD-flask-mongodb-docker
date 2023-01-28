from dataclasses import dataclass


@dataclass
class GetUsersInputDTO:
    page      : int
    per_page  : int
    sort_field: str
    order_by  : str
    endpoint  : str
