from typing import Optional
from pydantic import BaseModel


class Tokens(BaseModel):
    """
    Pydantic модель, которая возвращается при успешном запросе по url адресу https://id.vk.com/oauth2/auth

    За работу с данным url адресом отвечают следующие классы:

    1)_ExchangeCodeToToken
    2)_RefreshAccessToken

    Подробнее:
    1)https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/api-integration/api-description#Poluchenie-cherez-kod-podtverzhdeniya
    2)https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/api-integration/api-description#Poluchenie-cherez-Refresh-token
    """

    refresh_token: str
    access_token: str
    token_type: str
    expires_in: int
    user_id: int
    state: str
    scope: str
    id_token: Optional[str] = None

    class Config:
        from_attributes = True
