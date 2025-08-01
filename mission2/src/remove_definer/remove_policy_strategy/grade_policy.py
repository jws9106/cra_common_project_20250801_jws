from mission2.src.remove_definer.remove_policy_strategy.interface_remove_policy import IRemovePolicy

class GradePolicy(IRemovePolicy):
    def satisfy_remove_condition(self) -> bool:
        return self.player.grade == "NORMAL"
