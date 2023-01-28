from app.api.user.domain.repository.user_repository__interface import IUserRepository
from app.api.user.infractucture.repositories.user__repository import UserRepository
from app.api.user.domain.value_objects.email__vo import EmailVO
from app.api.user.application.errors.user__error import app_error_message


class GetUserByEmailUseCase(UserRepository):
    def __init__(self):
        self.user_repository = UserRepository(IUserRepository)

    def execute(self, email: EmailVO) -> dict:

        user = self.user_repository.get_user_by_email(email)

        if user:
            return {
                'id'               : user.id_user.value,
                'name'             : user.name.value,
                'email'            : user.email.value,
                'registration_date': user.registration_date,
                'date_updated'     : user.date_updated
            }

        return app_error_message('user_not_found')
