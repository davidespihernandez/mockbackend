from app.modules.mockers.base import Mocker
from app.modules.data.users import objects


class UsersMocker(Mocker):
    objects = objects
