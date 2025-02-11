__all__ = ["BaseForRequests"]


class BaseForRequests:
    """
    Базовый класс для работы с API VK ID

    Проверяет, чтобы переданный объект был экземпляром VK_ID
    """
    def __init__(self, application):
        if application.__class__.__name__ != "VK_ID":
            raise Exception("Object must be an instance of VK_ID class")
        self._application = application
