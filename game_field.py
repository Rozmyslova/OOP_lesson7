def fill_game_field(game_field):
    for i in range(3):
        print(" ", game_field[i * 3 + 0], "|", game_field[i * 3 + 1], "|", game_field[i * 3 + 2])
        if i == 2:
            break
        print(" ", "_" * 10)
