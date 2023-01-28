from app.api.user.domain.value_objects.uuid__vo import UuidVO
from app.api.user.domain.repository.user_repository__interface import IUserRepository
from app.api.user.infractucture.repositories.user__repository import UserRepository
from app.api.user.application.errors.user__error import app_error_message


class DeleteUserUseCase(UserRepository):

    def __init__(self):
        self.user_repository = UserRepository(IUserRepository)

    def execute(self, id_: UuidVO ) -> dict:
        try:
            delete_user = self.user_repository.delete_user(id_)
            if delete_user == True: 
                return {
                    'msg':'User with ID {} has been removed.'.format(id_.value)
                }
            return app_error_message('user_delete')
        except:
            return app_error_message('failed_service_user_delete')

