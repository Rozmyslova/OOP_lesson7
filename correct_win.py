def correct_win(game_field):
    winner_combination = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for elements in winner_combination:
        if game_field[elements[0]] == game_field[elements[1]] == game_field[elements[2]]:
            return True
    return False
