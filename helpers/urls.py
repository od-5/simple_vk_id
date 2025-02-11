from ..exception import OnlyHTTPS, URINotTrusted


class TrustedURIs:
    """
    Вспомогательный валидационный класс.

    Проверяет, имеет ли ссылка префикс 'https://'.

    Все доверенный url адреса сохраняются в __dict__ через setattr
    """

    def __getattribute__(self, url_tag: str):
        """
        Перегруженный магический метод.

        Позволяет вернуть url адрес по тегу. В случае, если тега не существует, возбуждает ошибку URINotTrusted

        """
        try:
            url = object.__getattribute__(self, url_tag)
            return url
        except Exception as _:
            return URINotTrusted

    def __setattr__(self, url_tag: str, value: str):
        """
        Перегруженный магический метод.

        Позволяет установить url адрес по тегу.

        В случае, если url адрес не начинается с 'https://', возбуждает ошибку URINotTrusted
        """
        if not value.startswith("https://"):
            raise OnlyHTTPS
        object.__setattr__(self, url_tag, value)
