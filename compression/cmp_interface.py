import abc


class GenericCompressionInterface(abc.ABC):
    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def encode(self, input_str, *args, **kwargs):
        pass

    @abc.abstractmethod
    def decode(self, input_str, *args, **kwargs):
        pass
