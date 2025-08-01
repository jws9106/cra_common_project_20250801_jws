from mission2.src.remove_definer.remove_policy_strategy.interface_remove_policy import IRemovePolicy
from mission2.src.common_constants import WEDNESDAY
class WednesdayAttendPolicy(IRemovePolicy):
    def satisfy_remove_condition(self) -> bool:
        return self.player.attendance_count_day_of_week[WEDNESDAY] == 0
