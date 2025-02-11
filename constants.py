from enum import Enum


class Scopes(str, Enum):
    """
    Класс, представляющий собой список доступных разрешений,
    которые можно указать при инициализации VK ID SDK в клиентском приложении или при обмене refresh токена

    Подробнее: https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/work-with-user-info/scopes
    """
    DEFAULT = "vkid.personal_info"
    EMAIL = "email"
    PHONE = "phone"
    FRIENDS = "friends"
    WALL = "wall"
    GROUPS = "groups"
    STORIES = "stories"
    DOCS = "docs"
    PHOTOS = "photos"
    ADS = "ads"
    VIDEO = "video"
    STATUS = "status"
    MARKET = "market"
    PAGES = "pages"
    NOTIFICATIONS = "notifications"
    STATS = "stats"
    NOTES = "notes"


class URLS(str, Enum):
    """
    Класс, представляющий собой список url адресов для работы с сервисом VK ID
    """
    AUTH = "https://id.vk.com/oauth2/auth"
    REVOKE_TOKEN = "https://id.vk.com/oauth2/revoke"
    LOGOUT = "https://id.vk.com/oauth2/logout"
    HIDDEN_USER_INFO = "https://id.vk.com/oauth2/public_info"
    USER_INFO = "https://id.vk.com/oauth2/user_info"


class GrantTypes(str, Enum):
    """
    Класс, отвечающий за параметр 'grant_type', отправляемый при запросах на получение токенов
    """
    AUTHORIZATION_CODE = "authorization_code"
    REFRESH_TOKEN = "refresh_token"


DEFAULT_HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}
