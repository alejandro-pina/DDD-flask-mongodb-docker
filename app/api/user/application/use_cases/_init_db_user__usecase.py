from app.api.user.domain.repository.user_repository__interface import IUserRepository
from app.api.user.infractucture.repositories.user__repository import UserRepository
from app.api.user.domain.models.user_model import UserModel
from app.api.user.domain.value_objects.uuid__vo import UuidVO
from app.api.user.domain.value_objects.idx__vo import IdxVO
from app.api.user.domain.value_objects.name__vo import NameVO
from app.api.user.domain.value_objects.email__vo import EmailVO
from app.api.user.domain.value_objects.password__vo import PasswordVO
from app.api.user.domain.value_objects.date__vo import DateVO
from app.api.user.domain.value_objects.short_str__vo import ShortStrVO
from app.api.user.application.errors.user__error import app_error_message


class InitDBUserUseCase(UserRepository):

    def __init__(self):
        self.user_repository = UserRepository(IUserRepository)

    def execute(self, id_: UuidVO, name: NameVO, email: EmailVO, password: PasswordVO, date_updated: DateVO, registration_date: DateVO) -> dict:

        email_exist = self.user_repository.get_user_by_email(email)
        if bool(email_exist):
            return {
                'error': 'Admin with mail {} exist.'.format(email.value)
            }
        field_name = ShortStrVO('email')
        index_name = ShortStrVO('unique_email')

        self.user_repository.create_index_field(field_name, index_name)

        field_idx = ShortStrVO('idx_users')
        idx = IdxVO(self.user_repository.get_idx(1, field_idx))
        if not idx:
            idx = IdxVO(self.user_repository.get_idx(0, field_idx))
        id_user = id_

        if self.user_repository.create_index_field(field_name, index_name):
            password = PasswordVO.create_hash(password.value)

            domain_user = UserModel(
                id_user, idx, name, email, password, registration_date, date_updated)
            new_user = self.user_repository.create_user(domain_user)

            if new_user:
                return {
                    'msg': 'Admin with mail {} has created.'.format(email.value)
                }
        return {
            'error': 'Error to create admin with mail {}.'.format(email.value)
        }
