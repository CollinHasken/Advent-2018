players = 403


def part_1(last_marble):
    player_scores = [0 for x in range(players)]
    current_player = 2
    marbles = [0, 2, 1]
    current_marble_pos = 1
    for marble in range(3, last_marble + 1):
        current_player += 1
        if current_player == players:
            current_player = 0
        if marble % 23 == 0:
            player_scores[current_player] += marble
            prev_marble = current_marble_pos - 7
            if prev_marble < 0:
                prev_marble = len(marbles) + prev_marble
            player_scores[current_player] += marbles.pop(prev_marble)
            current_marble_pos = prev_marble
            continue
        current_marble_pos += 1
        if current_marble_pos >= len(marbles):
            current_marble_pos -= len(marbles)
        current_marble_pos += 1
        marbles.insert(current_marble_pos, marble)
        if marble % 10000 == 0:
            print(marble)
    print(max(player_scores))


def part_2(last_marble):
    part_1(last_marble)
    return


if __name__ == '__main__':
    part = int(input("Which part?"))
    if part == 1:
        part_1(71920)
    else:
        part_2(7192000)
