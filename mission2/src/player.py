from collections import defaultdict
from mission2.src.common_constants import DAYS_OF_WEEK

class Player:
    player_instances_map: dict[str:object] = {}
    last_player_id: int = 0

    def __repr__(self):
        return f"NAME : {self.name}, POINT : {self.points}, GRADE : {self.grade}"

    @classmethod
    def get_instance(cls, name):
        if name not in cls.player_instances_map:
            cls.player_instances_map[name] = cls(name)

        return cls.player_instances_map[name]

    @classmethod
    def get_new_id(cls):
        cls.last_player_id += 1
        return cls.last_player_id

    def __init__(self, name: str):
        self.id = self.get_new_id()
        self.name = name
        self.points = 0
        self.grade = ""
        self.is_removed_player = False
        self.attendance_count_day_of_week = defaultdict(lambda: 0)

    def attend_by_day(self, day_of_week):
        if day_of_week not in DAYS_OF_WEEK:
            raise KeyError(f"Unknown day of week: {day_of_week}")

        day_index = DAYS_OF_WEEK.index(day_of_week)
        self.attendance_count_day_of_week[day_index] += 1


