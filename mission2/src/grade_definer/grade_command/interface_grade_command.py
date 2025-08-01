from abc import ABC, abstractmethod

class IGrade(ABC):
    registry = {}

    def __init__(self, points):
        self.points = points

    def __init_subclass__(cls):
        super().__init_subclass__()
        if hasattr(cls, "GRADE_NAME"):
            cls.registry[cls.GRADE_NAME] = cls

    @abstractmethod
    def is_valid(self):
        ...