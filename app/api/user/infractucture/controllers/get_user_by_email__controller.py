from app.api.user.domain.value_objects.email__vo import EmailVO
from app.api.user.application.use_cases.get_user_by_email__usecase import GetUserByEmailUseCase
from app.api.user.infractucture.errors.user__error import infractuture_user_error_message


class GetUserByEmailController:

    def __init__(self, email: str, get_user_by_email: GetUserByEmailUseCase = GetUserByEmailUseCase()) -> dict:
        self.email = EmailVO(email)
        self.get_user_by_email = get_user_by_email

    def execute(self) -> dict:
        users_found = self.get_user_by_email.execute(
            email=self.email,
        )
        if users_found:
            print(users_found)
            if 'registration_date' in users_found:
                registration_date = users_found['registration_date']
                users_found['registration_date'] = registration_date.date_convert_europe()
            if 'date_updated' in users_found:
                date_updated = users_found['date_updated']
                users_found['date_updated'] = date_updated.date_convert_europe()

            return users_found

        return infractuture_user_error_message('user_model')
