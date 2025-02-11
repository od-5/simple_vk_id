from vk_id.helpers.urls import TrustedURIs
from vk_id.helpers.credentials import String, ClientID
from vk_id.requests.auth import _ExchangeCodeToToken
from vk_id.requests.user_info import _GetUserPublicInfo
from vk_id.requests.refresh import _RefreshAccessToken


class VK_ID:
    """
    Класс для работы с API VK ID

    Собирает в себе все подклассы для работы с API
    """
    client_id = ClientID()
    client_secret = String()
    client_access_key = String()
    app_name = String()

    def __init__(
            self,
            client_id: str,
            client_secret: str,
            client_access_key: str,
            app_name: str
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_access_key = client_access_key
        self.app_name = app_name
        self.trusted_uris = TrustedURIs()
        self._code_exchanger = _ExchangeCodeToToken(self)
        self._user_info = _GetUserPublicInfo(self)
        self._token_refresher = _RefreshAccessToken(self)