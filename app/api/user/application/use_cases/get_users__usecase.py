from app.api.user.domain.repository.user_repository__interface import IUserRepository
from app.api.user.domain.value_objects.order_by__vo import OrderByVO
from app.api.user.domain.value_objects.page__vo import PageVO
from app.api.user.application.libs.helper_pagination__lib import get_total_pages
from app.api.user.domain.value_objects.sort_by__vo import SortByVO
from app.api.user.infractucture.repositories.user__repository import UserRepository
from app.api.user.application.errors.user__error import app_error_message


class GetUsersUseCase(UserRepository):

    def __init__(self):
        self.user_repository = UserRepository(IUserRepository)

    def execute(self, page: PageVO, per_page: PageVO, order_by: OrderByVO, sort_field: SortByVO) -> dict:
        try:
            count_user = self.user_repository.count_user_found('', '')

            if count_user == 0:
                return app_error_message('user_not_found')

            get_users = self.user_repository.get_users(
                page, per_page, order_by, sort_field)

            if get_users:

                users = []

                for user in get_users:
                    users.append(
                        {
                            'id_user'          : user.id_user.value,
                            'name'             : user.name.value,
                            'email'            : user.email.value,
                            'registration_date': user.registration_date,
                            'date_updated'     : user.date_updated
                        }
                    )

                return {
                    'users': users,
                    'total': count_user
                }

            # EXTRA: Helper user
            if count_user and (count_user > 0 and page.value > 1):
                return {
                    'error': 'User not found.',
                    'last_page': get_total_pages(per_page.value, count_user)
                }

            return app_error_message('user_not_found')
        except:
            return app_error_message('failed_service_get_user')
