import pytest
import random

from mission2.src.point_calculator.point_strategy.reset_point_strategy import ResetPointStrategy
from mission2.src.point_calculator.point_strategy.base_point_strategy import BasePointStrategy
from mission2.src.point_calculator.point_strategy.bonus_point_strategy import BonusPointStrategy
from mission2.src.point_calculator.point_calculator import PointCalculator
from mission2.src.player import Player

player_cnt = 0
def get_new_player_name():
    global player_cnt
    player_cnt += 1
    return f"NONAME_{player_cnt}"


@pytest.fixture
def initiate_player_list():
    Player.player_instances_map = {}
    yield
    Player.player_instances_map = {}


def test__reset_point_strategy(initiate_player_list):
    for i in range(30):
        player = Player.get_instance(name=get_new_player_name())
        player.points = random.randint(3, 10)

    ResetPointStrategy().execute()

    assert sum(p.points for p in Player.player_instances_map.values()) == 0

@pytest.mark.parametrize(
    "expected_point, days",[
        [1, ("monday",)],
        [1, ("tuesday",)],
        [3, ("wednesday",)],
        [1, ("thursday",)],
        [1, ("friday",)],
        [2, ("saturday",)],
        [2, ("sunday",)],
    ]
)
def test__base_attendance(initiate_player_list, expected_point, days):
    player = Player.get_instance(name="NONAME")
    for day in days:
        player.attend_by_day(day)

    BasePointStrategy().execute()
    assert player.points == expected_point


@pytest.mark.parametrize(
    "days, expected", [
        [ ["monday"] * 5, 0],
        [ ["monday"] * 10, 0],
        [ ["wednesday"] * 9, 0],
        [ ["wednesday"] * 10, 10],
        [ ["wednesday"] * 11, 10],
        [ ["saturday"] * 9, 0],
        [ ["saturday"] * 10, 10],
        [ ["saturday"] * 11, 10],
        [ ["saturday"] * 5 + ["sunday"] * 5, 10],
    ]
)
def test__bonus_point_strategy(initiate_player_list, days, expected):
    player = Player.get_instance(name="NONAME")
    for day in days:
        player.attend_by_day(day)

    BonusPointStrategy().execute()

    assert player.points == expected


def test__point_calculator(initiate_player_list):
    player = Player.get_instance(name="NONAME")
    days = (
        ["monday"] * 7 +
        ["tuesday"] * 8 +
        ["wednesday"] * 12 +
        ["thursday"] * 13 +
        ["friday"] * 14 +
        ["saturday"] * 9 +
        ["sunday"] * 8
    )
    for day in days:
        player.attend_by_day(day)

    PointCalculator.execute()

    assert player.points == 132







