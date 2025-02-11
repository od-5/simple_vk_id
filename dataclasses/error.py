from typing import Optional
from pydantic import BaseModel


class Error(BaseModel):
    """
    Pydantic модель, содержащая общее описание ошибки сервиса VK ID

    SDK возвращает объект данного класса при возникновении ошибки во время запроса.

    Подробнее:
    1)https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/api-integration/api-description#Zapros-vypolnen-s-oshibkoj

    """
    error: str
    error_description: str
    state: Optional[str] = None  # Опциональный параметр, который приходит только в некоторых типах ошибок
