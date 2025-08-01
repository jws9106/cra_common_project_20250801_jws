import pytest
from mission2.src.grade_definer.grade_definer import GradeDefiner
from mission2.src.player import Player

@pytest.fixture
def initiate_player_list():
    Player.player_instances_map = {}
    yield
    Player.player_instances_map = {}

@pytest.mark.parametrize(
    "points, expected_grade", (
        (0, "NORMAL"),
        (15, "NORMAL"),
        (29, "NORMAL"),
        (30, "SILVER"),
        (31, "SILVER"),
        (49, "SILVER"),
        (50, "GOLD"),
        (51, "GOLD"),
        (132, "GOLD")
    )
)
def test__grade(initiate_player_list, points, expected_grade):
    player = Player.get_instance(name="NONAME")
    player.points = points
    GradeDefiner.execute()
    assert player.grade == expected_grade







