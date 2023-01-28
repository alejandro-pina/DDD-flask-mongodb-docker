from app.api.user.domain.value_objects.uuid__vo import UuidVO
from app.api.user.domain.value_objects.name__vo import NameVO
from app.api.user.domain.value_objects.email__vo import EmailVO
from app.api.user.domain.value_objects.password__vo import PasswordVO
from app.api.user.domain.value_objects.date__vo import DateVO
from app.api.user.application.use_cases.update_user__usecase import UpdateUserUseCase


class UpdateUserController:

    def __init__(self, dto: dict, update_user: UpdateUserUseCase = UpdateUserUseCase()) -> dict:
        self.update_user = update_user
        self.id_         = UuidVO(dto.id)
        self.dto         = dto
        self.user_data   = {}

    def execute(self):
        date_updated = DateVO.today_europe_str()
        self.user_data['date_updated'] = DateVO.today()

        if self.dto.name:
            self.user_data['name'] = NameVO(self.dto.name)
        if self.dto.email:
            self.user_data['email'] = EmailVO(self.dto.email)
        if self.dto.password:
            self.user_data['password'] = PasswordVO(self.dto.password)

        update_user = self.update_user.execute(self.id_, self.user_data)
        if 'error' in update_user:
            return update_user

        update_user['date_updated'] = date_updated
        return update_user
