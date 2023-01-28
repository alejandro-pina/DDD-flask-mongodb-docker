from app.auth.domain.value_objects.email__vo import EmailVO
from app.auth.domain.value_objects.password__vo import PasswordVO
from app.api.user.application.use_cases.get_user_by_email_for_auth__usecase import GetUserByEmailForAuthUseCase
from app.auth.application.errors.auth__error import auth_app_error_message


class AuthUseCase:
    def __init__(self):
        self.get_user_by_email__usecase = GetUserByEmailForAuthUseCase()

    def execute(self, email: EmailVO, password: PasswordVO) -> dict:

        user = self.get_user_by_email__usecase.execute(email)
        if not bool(user) or 'error' in user:
            return auth_app_error_message('user_data')

        if not 'password' in user or not PasswordVO.compare_hash(password.value, user['password']):
            return auth_app_error_message('user_data')

        user_id = user['id']
        user_name = user['name']

        return {
            'id': user_id,
            'name': user_name
        }
