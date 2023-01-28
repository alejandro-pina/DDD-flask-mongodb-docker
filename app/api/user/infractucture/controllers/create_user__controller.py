from app.api.user.domain.value_objects.uuid__vo import UuidVO
from app.api.user.domain.value_objects.name__vo import NameVO
from app.api.user.domain.value_objects.email__vo import EmailVO
from app.api.user.domain.value_objects.password__vo import PasswordVO
from app.api.user.domain.value_objects.date__vo import DateVO
from app.services.uuid__service import UuidService
from app.api.user.application.use_cases.create_user__usecase import CreateUserUseCase


class CreateUserController:

    def __init__(self, dto: dict, create_user: CreateUserUseCase = CreateUserUseCase()) -> dict:
        self.name        = NameVO(dto.name)
        self.email       = EmailVO(dto.email)
        self.password    = PasswordVO(dto.password)
        self.create_user = create_user

    def execute(self):
        create_user = self.create_user.execute(
            id_               = UuidVO(UuidService.generate_uuid()),
            name              = self.name,
            email             = self.email,
            password          = self.password,
            date_updated      = DateVO.today(),
            registration_date = DateVO.today()
        )
        if 'error' in create_user:
            return create_user

        try:
            if 'registration_date' in create_user:
                registration_date = create_user['registration_date']
                create_user['registration_date'] = registration_date.date_convert_europe()
            if 'date_updated' in create_user:
                date_updated = create_user['date_updated']
                create_user['date_updated'] = date_updated.date_convert_europe()
        except:
            pass
        return create_user
