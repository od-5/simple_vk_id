class String:
    """
    Вспомогательный валидационный класс, имплементирующий структуре дескриптора
    """

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError(f"{self.name.replace('__', '')} must be a string")

        if not bool(len(value)):
            raise ValueError(f"{self.name.replace('__', '')} cannot be empty")

        setattr(instance, self.name, value)

    def __delete__(self, instance):
        pass


class ClientID(String):
    """
    Вспомогательный валидатационный класс, имплементирующий структуре дескриптора
    """

    def __set__(self, instance, value: str):

        if not type(value) == str:
            raise ValueError("Client ID must be a string")

        if not bool(len(value)):
            raise ValueError("Client ID cannot be empty")

        if not value.isdigit():
            raise ValueError("Client ID must contain only numeric values")

        setattr(instance, f"{self.name}", value)
