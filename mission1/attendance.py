import pathlib

ATTENDANCE_INPUT_PATH = pathlib.Path(__file__).parent / "attendance_weekday_500.txt"
DAYS_OF_WEEK = ['monday', 'tuesday', "wednesday", "thursday", "friday", "saturday", "sunday"]
WEDNESDAY = DAYS_OF_WEEK.index('wednesday')
SATURDAY = DAYS_OF_WEEK.index('saturday')
SUNDAY = DAYS_OF_WEEK.index('sunday')
NAME_OF_GRADE = ['NORMAL', 'GOLD', 'SILVER']

player_id_map: dict[str:int] = {}
last_player_id = 0

# dat[사용자ID][요일]:
attendance_count_by_day_of_week = [[0] * 100 for _ in range(100)]
attendance_points = [0] * 100
player_grade = [0] * 100
attendance_name_list = [''] * 100


def main() -> None:
    if not ATTENDANCE_INPUT_PATH.exists():
        print("파일을 찾을 수 없습니다.")
        return

    read_and_count_attendance_from_input_file()
    add_additional_points()
    define_attendance_grade()
    print_attendance_result()
    print_removed_players()


def add_attendance_points(player_name: str, day_of_week: str) -> None:
    player_id = get_player_id(player_name)

    if day_of_week in ("saturday", "sunday"):
        add_point = 2
    elif day_of_week == "wednesday":
        add_point = 3
    else:
        add_point = 1
    attendance_points[player_id] += add_point

    index = DAYS_OF_WEEK.index(day_of_week)
    attendance_count_by_day_of_week[player_id][index] += 1


def get_player_id(player_name):
    global last_player_id

    if player_name not in player_id_map:
        last_player_id += 1
        player_id_map[player_name] = last_player_id
        attendance_name_list[last_player_id] = player_name

    return player_id_map[player_name]


def read_and_count_attendance_from_input_file() -> bool:
    for line in ATTENDANCE_INPUT_PATH.read_text(encoding='utf-8').splitlines(keepends=False):
        parts = line.strip().split()
        if len(parts) == 2:
            add_attendance_points(player_name=parts[0], day_of_week=parts[1])


def add_additional_points():
    for player_id in range(1, last_player_id + 1):
        if is_over_9_days_attend_on_wednesday(player_id):
            attendance_points[player_id] += 10

        if is_over_9_days_attend_on_weekend(player_id):
            attendance_points[player_id] += 10


def is_over_9_days_attend_on_wednesday(player_id: int) -> bool:
    return attendance_count_by_day_of_week[player_id][WEDNESDAY] > 9


def is_over_9_days_attend_on_weekend(player_id: int) -> bool:
    saturday_attend_count = attendance_count_by_day_of_week[player_id][SATURDAY]
    sunday_attend_count = attendance_count_by_day_of_week[player_id][SUNDAY]
    return saturday_attend_count + sunday_attend_count > 9


def define_attendance_grade():
    for player_id in range(1, last_player_id + 1):
        if attendance_points[player_id] >= 50:
            player_grade[player_id] = 1
        elif attendance_points[player_id] >= 30:
            player_grade[player_id] = 2
        else:
            player_grade[player_id] = 0


def print_attendance_result():
    for player_id in range(1, last_player_id + 1):
        print(
            "NAME : {}, POINT : {}, GRADE : {}".format(
                attendance_name_list[player_id],
                attendance_points[player_id],
                NAME_OF_GRADE[player_grade[player_id]]
            )
        )


def print_removed_players():
    print("\nRemoved player")
    print("==============")
    for player_id in range(1, last_player_id + 1):

        if player_grade[player_id] != NAME_OF_GRADE.index("NORMAL"):
            continue

        if attendance_count_by_day_of_week[player_id][WEDNESDAY] > 0:
            continue

        if attendance_count_by_day_of_week[player_id][SATURDAY] > 0:
            continue

        if attendance_count_by_day_of_week[player_id][SUNDAY] > 0:
            continue

        print(attendance_name_list[player_id])


if __name__ == "__main__":
    main()
