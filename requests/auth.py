import requests
import logging
from typing import Union

from vk_id.constants import (
    GrantTypes,
    URLS,
    DEFAULT_HEADERS,
)
from vk_id.dataclasses.error import Error
from vk_id.dataclasses.tokens import Tokens
from vk_id.requests._base import BaseForRequests


__all__ = ["_ExchangeCodeToToken"]


logger = logging.getLogger('test_log')


class _ExchangeCodeToToken(BaseForRequests):
    """
    Класс для обмена кода подтверждения на токены

    Подробнее: https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/api-integration/api-description#Poluchenie-cherez-kod-podtverzhdeniya
    """

    def __call__(self,
                 code_verifier: str,
                 redirect_uri: str,
                 code: str,
                 device_id: str,
                 state: str) -> Union[Tokens, Error]:
        """
        Запрос для обмена device_id, code, state на пару токенов.
        """

        data = {
            "grant_type": GrantTypes.AUTHORIZATION_CODE.value,
            "code_verifier": code_verifier,
            "redirect_uri": redirect_uri,
            "code": code,
            "client_id": self._application.client_id,
            "device_id": device_id,
            "state": state
        }

        resp = requests.post(url=URLS.AUTH.value, headers=DEFAULT_HEADERS, data=data)
        response_body = resp.json()
        if response_body.get("error", False):
            logger.error('VK GET TOKENS => ', response_body)
            return Error(**response_body)
        return Tokens(**response_body)
