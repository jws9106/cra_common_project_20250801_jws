import pytest
from mission2.src.common_constants import WEDNESDAY, SATURDAY, SUNDAY
from mission2.src.player import Player

def test__객체생성_성공():
    sut = Player(name="James")
    assert sut.name == "James"

def test__same_name_same_object():
    sut1 = Player.get_instance(name="James")
    sut2 = Player.get_instance(name="James")

    assert sut1 == sut2

def test__diff_name_diff_object():
    sut1 = Player.get_instance(name="James")
    sut2 = Player.get_instance(name="Tomas")

    assert sut1 != sut2
    assert sut1.id != sut2.id


def test__print_stdout(capsys):
    sut = Player.get_instance(name="tester")
    print(sut)

    expected = "NAME : tester, POINT : 0, GRADE : \n"
    captured = capsys.readouterr()

    assert captured.out == expected

def test__attend_by_day():
    sut = Player.get_instance(name="tester")
    sut.attend_by_day("wednesday")
    sut.attend_by_day("wednesday")
    sut.attend_by_day("wednesday")
    sut.attend_by_day("saturday")
    sut.attend_by_day("saturday")
    sut.attend_by_day("sunday")

    assert sut.attendance_count_day_of_week[WEDNESDAY] == 3
    assert sut.attendance_count_day_of_week[SATURDAY] == 2
    assert sut.attendance_count_day_of_week[SUNDAY] == 1

def test__attend_by_day_fail():
    sut = Player.get_instance(name="tester")
    with pytest.raises(KeyError):
        sut.attend_by_day("wedndesday")
