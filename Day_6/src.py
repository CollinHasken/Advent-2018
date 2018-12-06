
def coord_xy(x, y, width):
    return x + (y * width)


def coord(xy, width):
    return xy % width, xy // width


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


min_x = 47
min_y = 47
grid_width = 283
grid_height = 266


def part_1():
    with open("Day_6/part1.txt", 'r') as file:
        grid = [[] for x in range(grid_height * grid_width)]
        possible_coord = []
        # Record each closest point and it's manhattan distance to each grid point
        for line in file:
            possible_coord.append([line, 0])
            cur_x, cur_y = [int(x) for x in line.strip().split(",")]
            cur_x -= min_x
            cur_y -= min_y
            for point in range(len(grid)):
                cur_man = manhattan(cur_x, cur_y, *coord(point, grid_width))
                if grid[point] == []:
                    grid[point] = [(line, cur_man)]
                elif cur_man == grid[point][0][1]:
                    grid[point].append((line, cur_man))
                elif cur_man < grid[point][0][1]:
                    grid[point] = [(line, cur_man)]

        # Mark any point that touches the edge as infinite
        infinite_points = set()
        for x in range(grid_width):
            grid_point = grid[coord_xy(x, 0, grid_width)]
            if len(grid_point) == 1:
                infinite_points.add(grid_point[0])
            grid_point = grid[coord_xy(x, grid_height - 1, grid_width)]
            if len(grid_point) == 1:
                infinite_points.add(grid_point[0])
        for y in range(grid_height):
            grid_point = grid[coord_xy(0, y, grid_width)]
            if len(grid_point) == 1:
                infinite_points.add(grid_point[0])
            grid_point = grid[coord_xy(grid_width - 1, y, grid_width)]
            if len(grid_point) == 1:
                infinite_points.add(grid_point[0])

        # Remove unusable grid points and coords
        grid = [x for x in grid if len(x) == 1]
        possible_coord = [x for x in possible_coord if x[0] not in infinite_points]

        # Count areas
        for coord_point in possible_coord:
            for grid_point in grid:
                if grid_point[0][0] == coord_point[0]:
                    coord_point[1] += 1

        largest_area = max(possible_coord, key=lambda x: x[1])
        print(largest_area[1])


grid_width2 = grid_width + 100
grid_height2 = grid_height + 100


def part_2():
    with open("Day_6/part1.txt", 'r') as file:
        grid = [0 for x in range(grid_height2 * grid_width2)]
        for line in file:
            cur_x, cur_y = [int(x) for x in line.strip().split(",")]
            cur_x -= min_x
            cur_y -= min_y
            for point in range(len(grid)):
                grid[point] += manhattan(cur_x, cur_y, *coord(point, grid_width2))

        area = len([0 for x in grid if x < 10000])
        print(area)
        return



if __name__ == '__main__':
    part = int(input("Which part?"))
    if part == 1:
        part_1()
    else:
        part_2()
