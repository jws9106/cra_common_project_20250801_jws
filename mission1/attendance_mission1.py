import pathlib

ATTENDANCE_INPUT_FILE = "./attendance_weekday_500.txt"
DAY_OF_WEEK_LIST = ['monday', 'tuesday', "wednesday", "thursday", "friday", "saturday", "sunday"]
IDX_WEDNESDAY = DAY_OF_WEEK_LIST.index('wednesday')
IDX_SATURDAY = DAY_OF_WEEK_LIST.index('wednesday')
IDX_SUNDAY = DAY_OF_WEEK_LIST.index('sunday')

attendance_dict: dict[int:str] = {}
latest_attendance_id = 0

# dat[사용자ID][요일]:
attendance_count_by_day_of_week = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [0] * 100
attendance_name_list = [''] * 100
wed = [0] * 100
weeken = [0] * 100

def input2(attendance_name, day_of_week):
    global latest_attendance_id

    if attendance_name not in attendance_dict:
        latest_attendance_id += 1
        attendance_dict[attendance_name] = latest_attendance_id
        attendance_name_list[latest_attendance_id] = attendance_name

    current_attendance_id = attendance_dict[attendance_name]

    if day_of_week in ("saturday", "sunday"):
        add_point = 2
        weeken[current_attendance_id] += 1
    elif day_of_week == "wednesday":
        add_point = 3
        wed[current_attendance_id] += 1
    else:
        add_point = 1

    index = DAY_OF_WEEK_LIST.index(day_of_week)
    attendance_count_by_day_of_week[current_attendance_id][index] += 1
    points[current_attendance_id] += add_point

def main():
    input_file_path = pathlib.Path(ATTENDANCE_INPUT_FILE)

    if not input_file_path.exists():
        print("파일을 찾을 수 없습니다.")
        return

    for line in input_file_path.read_text(encoding='utf-8').splitlines(keepends=False):
        parts = line.strip().split()
        if len(parts) == 2:
            input2(attendance_name=parts[0], day_of_week=parts[1])


    for attendance_id in range(1, latest_attendance_id + 1):
        if is_over_9_days_attend_on_wednesday(attendance_id):
            points[attendance_id] += 10

        if is_over_9_days_attend_on_weekend(attendance_id):
            points[attendance_id] += 10

        if points[attendance_id] >= 50:
            grade[attendance_id] = 1
        elif points[attendance_id] >= 30:
            grade[attendance_id] = 2
        else:
            grade[attendance_id] = 0

        print(f"NAME : {attendance_name_list[attendance_id]}, POINT : {points[attendance_id]}, GRADE : ", end="")
        if grade[attendance_id] == 1:
            print("GOLD")
        elif grade[attendance_id] == 2:
            print("SILVER")
        else:
            print("NORMAL")

    print("\nRemoved player")
    print("==============")
    for attendance_id in range(1, latest_attendance_id + 1):
        if grade[attendance_id] not in (1, 2) and wed[attendance_id] == 0 and weeken[attendance_id] == 0:
            print(attendance_name_list[attendance_id])

def is_over_9_days_attend_on_wednesday(attendance_id: int) -> bool:
    return attendance_count_by_day_of_week[attendance_id][IDX_WEDNESDAY] > 9

def is_over_9_days_attend_on_weekend(attendance_id: int) -> bool:
    saturday_attend_count = attendance_count_by_day_of_week[attendance_id][IDX_SATURDAY]
    sunday_attend_count = attendance_count_by_day_of_week[attendance_id][IDX_SUNDAY]
    return saturday_attend_count + sunday_attend_count > 9


if __name__ == "__main__":
    main()
