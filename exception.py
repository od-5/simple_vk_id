class WrongScopes(Exception):
    """
     Ошибка, которая возникает, когда передаются несуществующие scopes

     Подробнее смотреть механику класса ValidateScopes
    """
    def __init__(self, message="Non-existent scopes"):
        self.message = message
        super().__init__(self.message)


class AppAlreadyInitialized(Exception):
    """
    Ошибка, которая возникает, когда в пользовельском коде два раза конфигурируется приложение

    Возникает в функции configure_app
    """
    def __init__(self, message="App already initialized"):
        self.message = message
        super().__init__(self.message)


class AppNotInitialized(Exception):
    """
    Ошибка, которая возникает, когда в пользовельском коде не конфигурировано приложение

    Возникает в функциях:

    1)exchange_code
    2)get_user_public_info
    3)refresh_access_token
    """
    def __init__(self, message="App not initialized"):
        self.message = message
        super().__init__(self.message)


class OnlyHTTPS(Exception):
    """
    Ошибка, возникающая при передаче URL'ов, не имеющих протокола HTTPS

    Возникает в классе TrustedURIs
    """
    def __init__(self, message="Only HTTPS URL'S is allowed"):
        self.message = message
        super().__init__(self.message)


class URINotTrusted(Exception):
    """
    Ошибка возникающая при попытке получения url по несуществующему тегу

    Возникает в методе __getattribute__ класса TrustedURIs
    """
    def __init__(self, message="URI is not trusted"):
        self.message = message
        super().__init__(self.message)
