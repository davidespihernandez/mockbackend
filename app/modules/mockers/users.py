from app.modules.mockers.base import Mocker
from app.modules.test_data.users import objects


class UsersMocker(Mocker):
    objects = objects
