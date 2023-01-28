from app.auth.domain.value_objects.password__vo import PasswordVO
from app.auth.domain.value_objects.email__vo import EmailVO
from app.auth.application.use_cases.auth__usecase import AuthUseCase
from app.services.auth__service import AuthService

class AuthController:
    def __init__(self, dto: dict, login: AuthUseCase = AuthUseCase()):
        self.email           = EmailVO(dto.email)
        self.password        = PasswordVO(dto.password)
        self.login           = login
        
    def execute(self):

        login = self.login.execute(
            email       = self.email,
            password    = self.password
        )

        if login and not 'error' in login:
            id_    = login['id']
            name   = login['name']

            tokens = AuthService.signin(id_)
            tka    = tokens['tka']

            return {
                'name' : name,
                'tka'  : tka
            }

        return login
