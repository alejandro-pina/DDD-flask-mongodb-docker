from app.api.user.domain.value_objects.order_by__vo import OrderByVO
from app.api.user.domain.value_objects.page__vo import PageVO
from app.api.user.domain.value_objects.sort_by__vo import SortByVO
from app.api.user.application.use_cases.get_users__usecase import GetUsersUseCase
from app.api.user.infractucture.errors.user__error import infractuture_user_error_message


class GetUsersController:

    def __init__(self, dto: dict, get_users_use_case: GetUsersUseCase = GetUsersUseCase()) -> list:
        self.page               = PageVO(dto.page or 1)
        self.per_page           = PageVO(dto.per_page or 5)
        self.sort_field         = SortByVO(dto.sort_field or 'registration_date')
        self.order_by           = OrderByVO(dto.order_by or 'desc')
        self.endpoint           = dto.endpoint
        self.get_users_use_case = get_users_use_case

    def execute(self) -> dict:
        users_found = self.get_users_use_case.execute(
            page       = self.page,
            per_page   = self.per_page,
            order_by   = self.order_by,
            sort_field = self.sort_field
        )

        if(users_found):

            list_users = users_found['users'] if 'users' in users_found else []
            count_users_found = users_found['total'] if 'total' in users_found else 0

            if count_users_found == 0 or not isinstance(list_users, list):
                return users_found

            users = []
            for user in list_users:
                registration_date = user['registration_date']
                date_updated = user['date_updated']

                users.append(
                    {
                        'id'               : user['id_user'],
                        'name'             : user['name'],
                        'email'            : user['email'],
                        'registration_date': registration_date.date_convert_europe(),
                        'date_updated'     : date_updated.date_convert_europe()
                    }
                )

            return {
                'users'     : users,
                'total'     : count_users_found,
                'page'      : self.page.value,
                'per_page'  : self.per_page.value,
                'order_by'  : self.order_by.value,
                'sort_field': self.sort_field.value
            }

        return infractuture_user_error_message('user_model')
