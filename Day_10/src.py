import re


class point:
    def __init__(self, info):
        numbers = re.findall(r'-?\d+',info)
        self.position = int(numbers[0]), int(numbers[1])
        self.velocity = int(numbers[2]), int(numbers[3])

    def move(self):
        self.position = [sum(x) for x in zip(self.position, self.velocity)]
        return self.position

    def get_coord(self, width, mid):
        return mid[0] + self.position[0] + ((mid[1] + self.position[1]) * width)


def part_1():
    with open("Day_10/part1.txt", 'r') as file:
        points = []
        for line in file:
            points.append(point(line))
        a = False
        count = -1
        while True:
            max_pos = [0,0,0,0]
            for cur_point in points:
                if a:
                    new_pos = cur_point.move()
                else:
                    new_pos = cur_point.position
                if new_pos[0] < max_pos[0]:
                    max_pos[0] = new_pos[0]
                elif new_pos[0] > max_pos[1]:
                    max_pos[1] = new_pos[0]
                if new_pos[1] < max_pos[2]:
                    max_pos[2] = new_pos[1]
                elif new_pos[1] > max_pos[3]:
                    max_pos[3] = new_pos[1]
            a = True
            count += 1
            width = (max_pos[1] - max_pos[0]) + 1
            height = (max_pos[3] - max_pos[2]) + 1
            if width > 220 or height > 220:
                print(width, end=',')
                print(height)
                continue
            grid = ['.' for x in range (width * height)]
            mid = abs(max_pos[0]), abs(max_pos[2])
            for cur_point  in points:
                grid[cur_point.get_coord(width, mid)] = '#'
            for y in range(height):
                for x in range(width):
                    print(grid[x + (y * width)], end=' ')
                print('\n')
            input(str(count))




def part_2():
    with open("Day_10/part1.txt", 'r') as file:
        for line in file:

            return


if __name__ == '__main__':
    part = int(input("Which part?"))
    if part == 1:
        part_1()
    else:
        part_2()
