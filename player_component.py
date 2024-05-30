import abc


class PlayerComponent(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_reaction(self) -> dict:
        raise NotImplementedError

    @abc.abstractmethod
    def get_lives(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def get_diamonds(self) -> int:
        raise NotImplementedError
