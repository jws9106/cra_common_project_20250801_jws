import pathlib
from mission2.src.player import Player
from mission2.src.point_calculator.point_calculator import PointCalculator
from mission2.src.grade_definer.grade_definer import GradeDefiner
from mission2.src.remove_definer.remove_definer import RemoveDefiner


class AttendanceManager:
    def __init__(self, input_file_path):
        self.attendance_input_path = pathlib.Path(input_file_path)

    def execute(self):
        if not self.attendance_input_path.exists():
            raise FileNotFoundError("input_file_path가 존재하지 않습니다.: {self.attendance_input_path}")

        self.read_and_count_attendance_from_input_file()
        self.calculate_point_by_player()
        self.define_player_grade()
        self.define_is_removed_player()
        self.print_players()
        self.print_removed_players()

    def read_and_count_attendance_from_input_file(self):
        for line in self.attendance_input_path.read_text(encoding='utf-8').splitlines(keepends=False):
            parts = line.strip().split()
            if len(parts) == 2:
                player = Player.get_instance(name=parts[0])
                player.attend_by_day(parts[1])

    def calculate_point_by_player(self):
        PointCalculator.execute()

    def define_player_grade(self):
        GradeDefiner.execute()

    def define_is_removed_player(self):
        RemoveDefiner.execute()

    def print_players(self):
        for p in Player.player_instances_map.values():
            print(p)

    def print_removed_players(self):
        print("\nRemoved player")
        print("==============")

        for p in Player.player_instances_map.values():
            if p.is_removed_player:
                print(p.name)
