from app.api.user.domain.value_objects.uuid__vo import UuidVO
from app.api.user.domain.value_objects.name__vo import NameVO
from app.api.user.domain.value_objects.email__vo import EmailVO
from app.api.user.domain.value_objects.password__vo import PasswordVO
from app.api.user.domain.value_objects.date__vo import DateVO

from app.services.uuid__service import UuidService
from app.api.user.application.use_cases._init_db_user__usecase import InitDBUserUseCase


class InitDBController:

    def __init__(self, dto: dict, create_admin: InitDBUserUseCase = InitDBUserUseCase()) -> dict:
        self.name = NameVO(dto.name)
        self.email = EmailVO(dto.email)
        self.password = PasswordVO(dto.password)
        self.create_admin = create_admin

    def execute(self):
        print('\033[0m')
        print(
            '\033[93m ***********************************************************************')
        print('\033[93m  ⭐⭐⭐ InitDBController:')
        print(
            '\033[93m ***********************************************************************')
        print('\033[0m')

        try:
            create_admin = self.create_admin.execute(
                id_=UuidVO(UuidService.generate_uuid()),
                name=self.name,
                email=self.email,
                password=self.password,
                date_updated=DateVO.today(),
                registration_date=DateVO.today()
            )

            if 'error' in create_admin:
                print(
                    '\033[93m ***********************************************************************')
                print('\033[93m  ⭐🟡🟡 {}'.format(create_admin['error']))
                print(
                    '\033[93m ***********************************************************************')
            elif 'msg' in create_admin:
                print(
                    '\033[93m ***********************************************************************')
                print('\033[93m  ⭐🟢🟢 {}'.format(create_admin['msg']))
                print(
                    '\033[93m ***********************************************************************')
            else:
                print(
                    '\033[93m ***********************************************************************')
                print('\033[93m  ⭐🔴🔴 ERROR UNKNOW TO CREATE ADMIN.')
                print(
                    '\033[93m ***********************************************************************')
                raise ValueError('ERROR UNKNOW TO CREATE ADMIN.')
        except:
            print(
                '\033[93m ***********************************************************************')
            print('\033[93m  ⭐🔴🔴')
            print(
                '\033[93m ***********************************************************************')
            raise ValueError('Cant init db.')
