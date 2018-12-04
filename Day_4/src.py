import os


def part_1():
    with open("C:/Users/Collin/Documents/GitHub/Advent-2018/Day_4/part1.txt", 'r') as file:
        guards_shifts = {}
        for line in file:
            time = line.split("]")[0]
            info = line.split("]")[1]
            month = int(time.split("-")[1])
            date_time = time.split("-")[2]
            date = int(date_time.split(" ")[0])
            hour = int(date_time.split(" ")[1].split(":")[0])
            adjusted = False
            if hour != 0:
                adjusted = True
                time = 0
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
            else:
                time = int(date_time.split(" ")[1].split(":")[1])
            id = ''.join(x for x in info if x.isdigit())
            if id != '':
                id = int(id)
            asleep = info[1] == 'f'
            if month not in guards_shifts:
                guards_shifts[month] = {}
            if date not in guards_shifts[month]:
                guards_shifts[month][date] = [id, [0 for x in range(60)]]
            if id is not '':
                guards_shifts[month][date][0] = id
            if not asleep:
                if guards_shifts[month][date][1][time] == 3:
                    continue
                if guards_shifts[month][date][1][time] == 0:
                    if adjusted:
                        guards_shifts[month][date][1][time] = 0
                    else:
                        guards_shifts[month][date][1][time] = 2
                    continue

                if adjusted:
                    guards_shifts[month][date][1][time] = 0
                else:
                    guards_shifts[month][date][1][time] = 2

                for min in range(time + 1, 60):
                    if guards_shifts[month][date][1][min] == 3 or guards_shifts[month][date][1][min] == 2:
                        break
                    guards_shifts[month][date][1][min] = 0
            else:
                guards_shifts[month][date][1][time] = 3
                for min in range(time + 1, 60):
                    if guards_shifts[month][date][1][min] == 2 or guards_shifts[month][date][1][min] == 3:
                        break
                    guards_shifts[month][date][1][min] = 1
        sleep_count = {}
        for month, date_data in guards_shifts.items():
            for date, shift_data in date_data.items():
                if shift_data[0] not in sleep_count:
                    sleep_count[shift_data[0]] = 0
                sleep_count[shift_data[0]] += len([1 for x in shift_data[1] if x == 1 or x == 3])
        print(sleep_count)
        most_id = 0
        most_sleep = 0
        for id, sleep in sleep_count.items():
            if sleep > most_sleep:
                most_sleep = sleep
                most_id = id
        print(most_id)

        minutes = [0 for x in range(60)]
        for month, date_data in guards_shifts.items():
            for date, shift_data in date_data.items():
                if shift_data[0] == most_id:
                    for minute in range(60):
                        if shift_data[1][minute] == 1 or shift_data[1][minute] == 3:
                            minutes[minute] += 1
        print(minutes)
        maxs = 0
        for mins in range(60):
            if minutes[mins] > minutes[maxs]:
                maxs = mins
        print(maxs)
        print(most_id * maxs)


def part_2():
    with open("C:/Users/Collin/Documents/GitHub/Advent-2018/Day_4/part1.txt", 'r') as file:
        guards_shifts = {}
        for line in file:
            time = line.split("]")[0]
            info = line.split("]")[1]
            month = int(time.split("-")[1])
            date_time = time.split("-")[2]
            date = int(date_time.split(" ")[0])
            hour = int(date_time.split(" ")[1].split(":")[0])
            adjusted = False
            if hour != 0:
                adjusted = True
                time = 0
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
            else:
                time = int(date_time.split(" ")[1].split(":")[1])
            id = ''.join(x for x in info if x.isdigit())
            if id != '':
                id = int(id)
            asleep = info[1] == 'f'
            if month not in guards_shifts:
                guards_shifts[month] = {}
            if date not in guards_shifts[month]:
                guards_shifts[month][date] = [id, [0 for x in range(60)]]
            if id is not '':
                guards_shifts[month][date][0] = id
            if not asleep:
                if guards_shifts[month][date][1][time] == 3:
                    continue
                if guards_shifts[month][date][1][time] == 0:
                    if adjusted:
                        guards_shifts[month][date][1][time] = 0
                    else:
                        guards_shifts[month][date][1][time] = 2
                    continue

                if adjusted:
                    guards_shifts[month][date][1][time] = 0
                else:
                    guards_shifts[month][date][1][time] = 2

                for min in range(time + 1, 60):
                    if guards_shifts[month][date][1][min] == 3 or guards_shifts[month][date][1][min] == 2:
                        break
                    guards_shifts[month][date][1][min] = 0
            else:
                guards_shifts[month][date][1][time] = 3
                for min in range(time + 1, 60):
                    if guards_shifts[month][date][1][min] == 2 or guards_shifts[month][date][1][min] == 3:
                        break
                    guards_shifts[month][date][1][min] = 1

        minutes = {}
        for month, date_data in guards_shifts.items():
            for date, shift_data in date_data.items():
                if shift_data[0] not in minutes:
                    minutes[shift_data[0]] = [0 for x in range(60)]
                for minute in range(60):
                    if shift_data[1][minute] == 1 or shift_data[1][minute] == 3:
                        minutes[shift_data[0]][minute] += 1
        print(minutes)
        maxs = 0
        max_id = 0
        for id, mins in minutes.items():
            local_max = 0
            for min in range(60):
                if mins[min] > mins[local_max]:
                    local_max = min
            if max_id not in minutes or mins[local_max] > minutes[max_id][maxs]:
                max_id = id
                maxs = local_max
        print(maxs)
        print(max_id)
        print(max_id * maxs)


if __name__ == '__main__':
    part = int(input("Which part?"))
    if part == 1:
        part_1()
    else:
        part_2()
