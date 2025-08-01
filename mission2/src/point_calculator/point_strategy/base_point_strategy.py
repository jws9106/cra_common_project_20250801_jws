from mission2.src.point_calculator.point_strategy.interface_point_strategy import IPointStrategy
from mission2.src.player import Player
from mission2.src.common_constants import WEDNESDAY, SATURDAY, SUNDAY

class BasePointStrategy(IPointStrategy):
    EXEC_NUM = 100

    def execute(self):
        for player in Player.player_instances_map.values():
            player.points += self.get_default_point(player)

    def get_default_point(self, player:Player):
        point = 0
        for day_of_week, attendance_count in player.attendance_count_day_of_week.items():
            if day_of_week in (SATURDAY, SUNDAY):
                point += (2 * attendance_count)
            elif day_of_week == WEDNESDAY:
                point += (3 * attendance_count)
            else:
                point += attendance_count
        return point

