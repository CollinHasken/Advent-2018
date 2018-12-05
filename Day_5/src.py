import re


def part_1():
    with open("Day_5/part1.txt", 'r') as file:
        for line in file:
            line = line.strip() #fuck you whitespace
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            match_string = ''.join(''.join([char, char.upper(), '|', char.upper(), char, '|']) for char in alphabet)[:-1]
            match = re.compile(match_string)
            temp = match.sub('', line)
            while len(temp) != len(line):
                line = temp
                temp = match.sub('', line)
    print(len(line))


def part_2():
    with open("Day_5/part1.txt", 'r') as file:
        for line in file:
            line = line.strip()
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            match_string = ''.join(''.join([char, char.upper(), '|', char.upper(), char, '|']) for char in alphabet)[:-1]
            match = re.compile(match_string)
            least = len(line)
            for char in alphabet:
                test = re.sub(''.join([char, '|', char.upper()]), '', line)
                temp = match.sub('', test)
                while len(temp) != len(test):
                    test = temp
                    temp = match.sub('', test)
                if len(test) < least:
                    least = len(test)
    print(least)


if __name__ == '__main__':
    part = int(input("Which part?"))
    if part == 1:
        part_1()
    else:
        part_2()
