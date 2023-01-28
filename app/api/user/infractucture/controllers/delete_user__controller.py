from app.api.user.domain.value_objects.uuid__vo import UuidVO
from app.api.user.application.use_cases.delete_user__usecase import DeleteUserUseCase


class DeleteUserController:

    def __init__(self, id_: str,  delete_user: DeleteUserUseCase = DeleteUserUseCase()) -> dict:
        self.id_ = UuidVO(id_)
        self.delete_user = delete_user

    def execute(self):
        return self.delete_user.execute(self.id_)
