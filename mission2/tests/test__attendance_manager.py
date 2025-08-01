import os
import pathlib
import tempfile

import pytest
from mission2.src.attendance_manager import AttendanceManager
from mission2.src.player import Player

@pytest.fixture
def initiate_player_list():
    Player.player_instances_map = {}
    yield
    Player.player_instances_map = {}

@pytest.fixture
def sut():
    input_txt =  """
    Umar monday
    Umar monday
    Daisytuesday
    Alice tuesday
    Xena saturday
    Ian tuesday
    Hannah monday
    """
    temp_file = pathlib.Path("__file__").parent / "temp_input.txt"
    temp_file.write_text(input_txt)
    sut = AttendanceManager(temp_file)
    sut.read_and_count_attendance_from_input_file()
    yield sut
    temp_file.unlink()

def test_FoundNotFile(initiate_player_list):
    with pytest.raises(FileNotFoundError):
        AttendanceManager("NoExistsFile.txt").execute()

def test__read_and_count_attendance_from_input_file(initiate_player_list, sut):
    assert len(Player.player_instances_map) == 5

def test__calculate_point_by_player(initiate_player_list, sut):
    sut.calculate_point_by_player()
    assert sum(p.points for p in Player.player_instances_map.values()) == 7

def test__define_player_grade(initiate_player_list, sut):
    sut.calculate_point_by_player()
    sut.define_player_grade()
    assert set(p.grade for p in Player.player_instances_map.values()) == {"NORMAL"}

def test__define_is_removed_player(initiate_player_list, sut):
    sut.calculate_point_by_player()
    sut.define_player_grade()
    sut.define_is_removed_player()
    assert sum(p.is_removed_player for p in Player.player_instances_map.values()) == 4

def test__execute(initiate_player_list, sut, capsys):
    sut.execute()
    expected = """\
NAME : Umar, POINT : 4, GRADE : NORMAL
NAME : Alice, POINT : 2, GRADE : NORMAL
NAME : Xena, POINT : 4, GRADE : NORMAL
NAME : Ian, POINT : 2, GRADE : NORMAL
NAME : Hannah, POINT : 2, GRADE : NORMAL

Removed player
==============
Umar
Alice
Ian
Hannah
"""
    captured = capsys.readouterr()
    assert captured.out == expected


