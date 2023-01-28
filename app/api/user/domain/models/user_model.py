from app.api.user.domain.value_objects.uuid__vo import UuidVO
from app.api.user.domain.value_objects.idx__vo import IdxVO
from app.api.user.domain.value_objects.name__vo import NameVO
from app.api.user.domain.value_objects.email__vo import EmailVO
from app.api.user.domain.value_objects.password__vo import PasswordVO
from app.api.user.domain.value_objects.date__vo import DateVO


class UserModel:

    def __init__(self, id_user: UuidVO, idx: IdxVO, name: NameVO, email: EmailVO, password: PasswordVO, registration_date: DateVO, date_updated: DateVO, avatar=''):

        self.assert_is_valid(id_user, name, email, password, registration_date, date_updated)

        self.id_user           = id_user
        self.idx               = idx
        self.name              = name
        self.email             = email
        self.password          = password
        self.registration_date = registration_date
        self.date_updated      = date_updated
        self.avatar            = avatar

    def assert_is_valid(self, id_user, name, email, password, registration_date, date_updated):

        if not isinstance(id_user, UuidVO) or not isinstance(name, NameVO) or not isinstance(email, EmailVO) or not isinstance(password, PasswordVO) or not isinstance(registration_date, DateVO) and not isinstance(date_updated, DateVO):
            raise ValueError("Model error data.")
