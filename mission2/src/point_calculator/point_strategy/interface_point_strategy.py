from abc import abstractmethod, ABC

class IPointStrategy(ABC):
    registry = {}

    def __init_subclass__(cls):
        super().__init_subclass__()
        if hasattr(cls, "EXEC_NUM"):
            cls.registry[cls.EXEC_NUM] = cls

    @abstractmethod
    def execute(self):
        ...