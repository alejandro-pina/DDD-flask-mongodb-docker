from abc import ABC, abstractmethod
from typing import List, Optional
from ..models.user_model import UserModel

class IUserRepository(ABC):
    """IUserRepository defines a repository interface for Users entity."""

    @abstractmethod
    def count_user_found(self, search: str, field: str) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_users(self, name: str, page: int, per_page: int, order_by: str, sort_field: str, endpoint: str) -> list:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_id(self, id_: str) -> Optional[UserModel]:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[UserModel]:
        raise NotImplementedError

    @abstractmethod
    def get_idx(self, start: int, field_name: str) -> int:
        raise NotImplementedError

    @abstractmethod
    def create_index_field(self, field_name: str, index_name: str) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def create_user(self, domain_user: dict) -> dict:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, id_: str, update_data: dict) -> bool:
        raise NotImplementedError
        
    @abstractmethod
    def delete_user(self, id_: str) -> bool:
        raise NotImplementedError

