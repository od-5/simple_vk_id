import datetime
from typing import Optional, Union
from enum import Enum

from pydantic import BaseModel, field_validator


class Gender(str, Enum):
    """
    Вспомогательный класс для удобной конвертации пола пользователя
    """
    MAN = "man"
    WOMAN = "woman"
    UNDEFINED = "undefined"


class User(BaseModel):
    """
    Pydantic модель, содержащая информацию о пользователе

    В зависимости от указанных прав при обмене кода, некоторые поля могут присутсвовать или отсутствовать.

    Подробнее: https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/api-integration/api-description#Poluchenie-nemaskirovannyh-dannyh
    """
    user_id: Optional[Union[int, str]] = None
    first_name: str
    last_name: str
    avatar: str
    sex: Union[int, str]
    birthday: Union[str, datetime.date]
    phone: Optional[str] = None
    email: Optional[str] = None
    sex: Optional[int] = None
    verified: bool

    @field_validator("user_id")
    def check_user_id(cls, user_id: str):
        return int(user_id)

    @field_validator("sex")
    @classmethod
    def check_sex(cls, v):
        if v == 1:
            return Gender.WOMAN.value
        elif v == 2:
            return Gender.MAN.value
        else:
            return Gender.UNDEFINED.value

    @field_validator("birthday")
    @classmethod
    def check_birthday(cls, v):
        return datetime.datetime.strptime(v, "%d.%m.%Y").date()

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        if v == '':
            return None
        return v
