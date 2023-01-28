from app.services.mongodb.userdb__mongodb import UserDB
from app.api.user.domain.repository.user_repository__interface import IUserRepository
from app.api.user.domain.models.user_model import UserModel
from app.api.user.domain.value_objects.short_str__vo import ShortStrVO
from app.api.user.domain.value_objects.date__vo import DateVO
from app.api.user.domain.value_objects.field_date__vo import FieldDateVO
from app.api.user.domain.value_objects.uuid__vo import UuidVO
from app.api.user.domain.value_objects.idx__vo import IdxVO
from app.api.user.domain.value_objects.name__vo import NameVO
from app.api.user.domain.value_objects.email__vo import EmailVO
from app.api.user.domain.value_objects.password__vo import PasswordVO

#    ✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅


class UserRepository(IUserRepository):
    def __init__(self, IUserRepository):
        self.execute = UserDB

    def to_domain(self, persistanceUser):

        return UserModel(
            id_user           = UuidVO(persistanceUser['id'] if 'id' in persistanceUser else persistanceUser['_id']),
            idx               = IdxVO(persistanceUser['idx']),
            name              = NameVO(persistanceUser['name']),
            email             = EmailVO(persistanceUser['email']),
            password          = PasswordVO(persistanceUser['password']),
            registration_date = DateVO(persistanceUser['registration_date']),
            date_updated      = DateVO(persistanceUser['date_updated'])
        )

    def to_persistance(self, domainUser):
        return {
            '_id'              : domainUser.id_user.value,
            'idx'              : domainUser.idx.value,
            'name'             : domainUser.name.value,
            'email'            : domainUser.email.value,
            'password'         : domainUser.password.value,
            'registration_date': domainUser.registration_date.value,
            'date_updated'     : domainUser.date_updated.value
        }

    def count_user_found(self, search: str, field: str) -> int:
        try:
            count_user_found = self.execute.count_user_found(
                search,
                field
            )
            if not count_user_found:
                return 0
            return count_user_found
        except:
            return 0

    def get_users(self, page: int, per_page: int, order_by: str, sort_field: str) -> dict:
        try:
            users_found = self.execute.get_users(
                page.value,
                per_page.value,
                order_by.value,
                sort_field.value
            )

            if not users_found:
                return {}

            users = []
            for user in users_found:
                users.append(self.to_domain(user))

            return users

        except:
            return {}

    def get_user_by_id(self, id_: UuidVO) -> dict:
        try:
            user_found = self.execute.get_user_by_id(
                id_.value
            )
            if not user_found:
                return {}
            return self.to_domain(user_found)
        except:
            return {}

    def get_user_by_email(self, email: EmailVO) -> dict:
        try:
            user_found = self.execute.get_user_by_email(
                email.value
            )
            if not user_found:
                return {}
            return self.to_domain(user_found)
        except:
            return {}

    def get_idx(self, start: int, field_name: ShortStrVO) -> int:
        try:
            return self.execute.get_user_idx(start, field_name.value)
        except:
            return 0

    def create_index_field(self, field_name: ShortStrVO, index_name: ShortStrVO) -> bool:
        try:
            create_unique_field = self.execute.create_index_field(
                field_name.value, index_name.value)
            if not create_unique_field:
                return False
            return True
        except:
            return False

    def create_user(self, domain_user: dict) -> dict:
        try:
            user = self.to_persistance(domain_user)
            new_user = self.execute.create_user(user)
            if not new_user:
                return {}
            return domain_user
        except:
            return {}

    def update_user(self, id_: UuidVO, update_data: dict) -> bool:
        try:
            if self.execute.update_user(id_.value, update_data) == True:
                return True
            return False
        except:
            return False

    def delete_user(self, id_: UuidVO) -> bool:
        try:
            if self.execute.delete_user(id_.value) == True:
                return True
            return False
        except:
            return False
