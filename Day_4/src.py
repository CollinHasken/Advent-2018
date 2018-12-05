import operator


def part_1():
    with open("part1.txt", 'r') as file:
        guards_shifts = {}
        for line in file:
            time, info = line.split("]")
            month, date_time = [date_info for date_info in time.split("-")[1:]]
            month = int(month)
            date, time = date_time.split(" ")
            date = int(date)
            hour, minutes = [int(d) for d in time.split(":")]
            if hour != 0:
                minutes = 0
                date += 1
                month_lim = 31
                if month == 4 or month == 6 or month == 9 or month == 11:
                    month_lim = 30
                if month == 2:
                    month_lim = 28
                if date > month_lim:
                    date = 1
                    month += 1
                if month == 13:
                    month = 1
            id = ''.join(x for x in info if x.isdigit())
            if id != '':
                id = int(id)
            asleep = info[1] == 'f'
            if month not in guards_shifts:
                guards_shifts[month] = {}
            if date not in guards_shifts[month]:
                guards_shifts[month][date] = [id, [0 for x in range(60)]]
            if id != '':
                guards_shifts[month][date][0] = id
            if not asleep:
                if guards_shifts[month][date][1][minutes] == 3:
                    continue
                if guards_shifts[month][date][1][minutes] == 0:
                    if hour != 0:
                        guards_shifts[month][date][1][minutes] = 0
                    else:
                        guards_shifts[month][date][1][minutes] = 2
                    continue

                if hour != 0:
                    guards_shifts[month][date][1][minutes] = 0
                else:
                    guards_shifts[month][date][1][minutes] = 2

                for min in range(minutes + 1, 60):
                    if guards_shifts[month][date][1][min] == 3 or guards_shifts[month][date][1][min] == 2:
                        break
                    guards_shifts[month][date][1][min] = 0
            else:
                guards_shifts[month][date][1][minutes] = 3
                for min in range(minutes + 1, 60):
                    if guards_shifts[month][date][1][min] == 2 or guards_shifts[month][date][1][min] == 3:
                        break
                    guards_shifts[month][date][1][min] = 1
        sleep_count = {}
        for month, date_data in guards_shifts.items():
            for date, shift_data in date_data.items():
                if shift_data[0] not in sleep_count:
                    sleep_count[shift_data[0]] = 0
                sleep_count[shift_data[0]] += shift_data[1].count(1) + shift_data[1].count(3)
        sorted_sleep_count = sorted(sleep_count.items(), key=operator.itemgetter(1), reverse=True)

        minutes = [0 for x in range(60)]
        for month, date_data in guards_shifts.items():
            for date, shift_data in date_data.items():
                if shift_data[0] == sorted_sleep_count[0][0]:
                    for minute in range(60):
                        if shift_data[1][minute] == 1 or shift_data[1][minute] == 3:
                            minutes[minute] += 1

        max_minute = max(enumerate(minutes), key=lambda m: m[1])[0]
        print(sorted_sleep_count[0][0] * max_minute)


def part_2():
    with open("C:/Users/Collin/Documents/GitHub/Advent-2018/Day_4/part1.txt", 'r') as file:
        guards_shifts = {}
        for line in file:
            time, info = line.split("]")
            month, date_time = [date_info for date_info in time.split("-")[1:]]
            month = int(month)
            date, time = date_time.split(" ")
            date = int(date)
            hour, minutes = [int(d) for d in time.split(":")]
            if hour != 0:
                minutes = 0
                date += 1
                month_lim = 31
                if month == 4 or month == 6 or month == 9 or month == 11:
                    month_lim = 30
                if month == 2:
                    month_lim = 28
                if date > month_lim:
                    date = 1
                    month += 1
                if month == 13:
                    month = 1
            id = ''.join(x for x in info if x.isdigit())
            if id != '':
                id = int(id)
            asleep = info[1] == 'f'
            if month not in guards_shifts:
                guards_shifts[month] = {}
            if date not in guards_shifts[month]:
                guards_shifts[month][date] = [id, [0 for x in range(60)]]
            if id != '':
                guards_shifts[month][date][0] = id
            if not asleep:
                if guards_shifts[month][date][1][minutes] == 3:
                    continue
                if guards_shifts[month][date][1][minutes] == 0:
                    if hour != 0:
                        guards_shifts[month][date][1][minutes] = 0
                    else:
                        guards_shifts[month][date][1][minutes] = 2
                    continue

                if hour != 0:
                    guards_shifts[month][date][1][minutes] = 0
                else:
                    guards_shifts[month][date][1][minutes] = 2

                for min in range(minutes + 1, 60):
                    if guards_shifts[month][date][1][min] == 3 or guards_shifts[month][date][1][min] == 2:
                        break
                    guards_shifts[month][date][1][min] = 0
            else:
                guards_shifts[month][date][1][minutes] = 3
                for min in range(minutes + 1, 60):
                    if guards_shifts[month][date][1][min] == 2 or guards_shifts[month][date][1][min] == 3:
                        break
                    guards_shifts[month][date][1][min] = 1

        minutes = {}
        for month, date_data in guards_shifts.items():
            for date, shift_data in date_data.items():
                if shift_data[0] not in minutes:
                    minutes[shift_data[0]] = [[x, 0] for x in range(60)]
                for minute in range(60):
                    if shift_data[1][minute] == 1 or shift_data[1][minute] == 3:
                        minutes[shift_data[0]][minute][1] += 1

        max_id, max_minutes = max(minutes.items(), key=lambda mins: max(mins[1], key=lambda m: m[1])[1])
        max_minute = max(max_minutes, key=lambda m: m[1])[0]
        print(max_id * max_minute)


if __name__ == '__main__':
    part = int(input("Which part?"))
    if part == 1:
        part_1()
    else:
        part_2()
