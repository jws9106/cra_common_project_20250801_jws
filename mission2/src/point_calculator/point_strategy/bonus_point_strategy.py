from mission2.src.point_calculator.point_strategy.interface_point_strategy import IPointStrategy
from mission2.src.player import Player
from mission2.src.common_constants import WEDNESDAY, SATURDAY, SUNDAY


class BonusPointStrategy(IPointStrategy):
    EXEC_NUM = 200

    def execute(self):
        for player in Player.player_instances_map.values():
            player.points += self.get_bouns_point(player)

    def get_bouns_point(self, player):
        point = 0

        if player.attendance_count_day_of_week[WEDNESDAY] > 9:
            point += 10

        cnt_attend_saturday = player.attendance_count_day_of_week[SATURDAY]
        cnt_attend_sunday = player.attendance_count_day_of_week[SUNDAY]
        if cnt_attend_saturday + cnt_attend_sunday > 9:
            point += 10

        return point
