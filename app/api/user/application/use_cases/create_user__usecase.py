from app.api.user.domain.models.user_model import UserModel
from app.api.user.domain.value_objects.uuid__vo import UuidVO
from app.api.user.domain.value_objects.idx__vo import IdxVO
from app.api.user.domain.value_objects.name__vo import NameVO
from app.api.user.domain.value_objects.email__vo import EmailVO
from app.api.user.domain.value_objects.password__vo import PasswordVO
from app.api.user.domain.value_objects.date__vo import DateVO
from app.api.user.domain.value_objects.short_str__vo import ShortStrVO
from app.api.user.domain.repository.user_repository__interface import IUserRepository
from app.api.user.infractucture.repositories.user__repository import UserRepository
from app.api.user.application.errors.user__error import app_error_message


class CreateUserUseCase(UserRepository):

    def __init__(self):
        self.user_repository = UserRepository(IUserRepository)

    def execute(self, id_: UuidVO, name: NameVO, email: EmailVO, password: PasswordVO, date_updated: DateVO, registration_date: DateVO) -> dict:

        try:

            email_exist = self.user_repository.get_user_by_email(email)
            if bool(email_exist):
                return app_error_message('email_exist')

            # IMPORTANT: in init app has been create index with email _init_db__usecase
            # field_name = ShortStrVO('email')
            # index_name = ShortStrVO('unique_email')
            # self.user_repository.create_index_field(field_name, index_name)

            # Get the next index
            field_idx = ShortStrVO('idx_users')
            idx = IdxVO(self.user_repository.get_idx(1, field_idx))
            if not idx:
                idx = IdxVO(self.user_repository.get_idx(0, field_idx))
            id_user = id_

            password = PasswordVO.create_hash(password.value)

            domain_user = UserModel(
                id_user, idx, name, email, password, registration_date, date_updated)
            new_user = self.user_repository.create_user(domain_user)

            if new_user:
                return {
                    'id': id_user.value,
                    'idx': idx.value,
                    'name': name.value,
                    'email': email.value,
                    'registration_date': registration_date,
                    'date_updated': date_updated
                }
            return app_error_message('user_create')
        except:
            return app_error_message('failed_service_user_user_create')
