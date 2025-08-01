from abc import ABC, abstractmethod

from mission2.src.player import Player


class IRemovePolicy(ABC):
    registry = []

    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.registry.append(cls)

    def __init__(self, player:Player):
        self.player = player

    @abstractmethod
    def satisfy_remove_condition(self) -> bool:
        ...