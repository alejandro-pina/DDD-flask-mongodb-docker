from app.api.user.domain.repository.user_repository__interface import IUserRepository
from app.api.user.domain.value_objects.uuid__vo import UuidVO
from app.api.user.domain.value_objects.password__vo import PasswordVO
from app.api.user.infractucture.repositories.user__repository import UserRepository
from app.api.user.application.errors.user__error import app_error_message


class UpdateUserUseCase(UserRepository):

    def __init__(self):
        self.user_repository = UserRepository(IUserRepository)

    def execute(self, id_: UuidVO, update_data: dict) -> dict:

        try:
            has_exist_user = self.user_repository.get_user_by_id(id_)

            if has_exist_user:
                if 'email' in update_data:
                    has_exist_email = self.user_repository.get_user_by_email(
                        update_data['email'])
                    if has_exist_email and has_exist_email.id_user != id_:
                        return app_error_message('email_exist')
                if 'password' in update_data:
                    update_data['password'] = PasswordVO.create_hash(
                        update_data['password'].value)
                for k, v in update_data.items():
                    update_data[k] = v.value

                update_user = self.user_repository.update_user(
                    id_, update_data)

                if update_user == True:
                    return {
                        'msg': 'User with ID {} has been updated.'.format(id_.value),
                        'updated_fields': list(update_data.keys())
                    }
                return app_error_message('user_update')

            return app_error_message('user_exist')

        except:
            return app_error_message('failed_service_user_update')
