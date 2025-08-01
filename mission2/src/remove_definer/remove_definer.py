from mission2.src.player import Player
from mission2.src.remove_definer.remove_policy_strategy.interface_remove_policy import IRemovePolicy


class RemoveDefiner:
    @classmethod
    def execute(cls):
        for player in Player.player_instances_map.values():
            player.is_removed_player = cls.is_removed_player(player)

    @classmethod
    def is_removed_player(cls, player:Player) -> bool:
        for policy_cls in IRemovePolicy.registry:
            if not policy_cls(player).satisfy_remove_condition():
                return False
        return True
