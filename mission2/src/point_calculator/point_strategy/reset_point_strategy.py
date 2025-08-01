from mission2.src.point_calculator.point_strategy.interface_point_strategy import IPointStrategy
from mission2.src.player import Player
from mission2.src.common_constants import WEDNESDAY, SATURDAY, SUNDAY

class ResetPointStrategy(IPointStrategy):
    EXEC_NUM = 0

    def execute(self):
        for player in Player.player_instances_map.values():
            player.points = 0
