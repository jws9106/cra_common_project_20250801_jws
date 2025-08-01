import pytest
import random

from mission2.src.common_constants import WEDNESDAY, SATURDAY, SUNDAY
from mission2.src.remove_definer.remove_definer import RemoveDefiner
from mission2.src.player import Player

@pytest.fixture
def initiate_player_list():
    Player.player_instances_map = {}
    yield
    Player.player_instances_map = {}

def test__remove_definer_removed(initiate_player_list):
    player = Player.get_instance(name="NONAME")
    player.grade = "NORMAL"
    player.attendance_count_day_of_week[WEDNESDAY] = 0
    player.attendance_count_day_of_week[SATURDAY] = 0
    player.attendance_count_day_of_week[SUNDAY] = 0

    RemoveDefiner.execute()
    assert player.is_removed_player == True


@pytest.mark.parametrize(
    "grade", ["GOLD", "SILVER"]
)
def test__remove_definer_stayed_by_grade(initiate_player_list, grade):
    player = Player.get_instance(name="NONAME")
    player.grade = grade

    RemoveDefiner.execute()
    assert player.is_removed_player == False


@pytest.mark.parametrize(
    "day", [WEDNESDAY, SATURDAY, SUNDAY]
)
def test__remove_definer_stayed_by_day(initiate_player_list, day):
    player = Player.get_instance(name="NONAME")
    player.grade = "NORMAL"
    player.attendance_count_day_of_week[day] = 1

    RemoveDefiner.execute()
    assert player.is_removed_player == False







