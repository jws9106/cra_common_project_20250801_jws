from mission2.src.grade_definer.grade_command.interface_grade_command import IGrade
from mission2.src.player import Player

class GradeDefiner:
    @classmethod
    def execute(cls):
        for player in Player.player_instances_map.values():
            player.grade = cls.get_grade(player)

    @classmethod
    def get_grade(cls, player:Player) -> str:
        for grade_name, grade_cls in IGrade.registry.items():
            if grade_cls(player.points).is_valid():
                return grade_name

        return "NORMAL"
