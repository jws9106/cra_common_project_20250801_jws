from mission2.src.remove_definer.remove_policy_strategy.interface_remove_policy import IRemovePolicy
from mission2.src.common_constants import SATURDAY, SUNDAY
class WeekendAttendPolicy(IRemovePolicy):
    def satisfy_remove_condition(self) -> bool:
        if self.player.attendance_count_day_of_week[SATURDAY] > 0:
            return False

        if self.player.attendance_count_day_of_week[SUNDAY] > 0:
            return False

        return True
