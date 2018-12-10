import re


class node:
    def __init__(self, input):
        self.child_amount = int(input[0])
        self.data_amount = int(input[1])
        self.children = []
        end_index = self.make_children(input[2:])
        self.store_data(input[end_index + 2:])

    def get_length(self):
        length = 2 + self.data_amount
        for child in self.children:
            length += child.get_length()
        return length

    def make_children(self, input):
        list_index = 0
        for index in range(self.child_amount):
            self.children.append(node(input[list_index:]))
            list_index += self.children[-1].get_length()
        return list_index

    def store_data(self, input):
        if self.data_amount == 0:
            self.data = []
        else:
            self.data = [int(num) for num in input[:self.data_amount]]

    def get_total_data(self):
        if self.data == []:
            data = 0
        else:
            data = sum(self.data)
        for child in self.children:
            data += child.get_total_data()
        return data

    def get_value(self):
        if self.data == []:
            return 0

        if len(self.children) == 0:
            return sum(self.data)

        value = 0
        for index in self.data:
            if index > self.child_amount or index <= 0:
                continue
            value += self.children[index - 1].get_value()
        return value


def part_1():
    with open("Day_8/part1.txt", 'r') as file:
        for line in file:
            head = node(re.findall('\d+', line))
            print(head.get_total_data())
            return


def part_2():
    with open("Day_8/part1.txt", 'r') as file:
        for line in file:
            head = node(re.findall('\d+', line))
            print(head.get_value())
            return


if __name__ == '__main__':
    part = int(input("Which part?"))
    if part == 1:
        part_1()
    else:
        part_2()
