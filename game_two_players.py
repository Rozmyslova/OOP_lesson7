from player_name import player_name
from game_field import fill_game_field
from correct_element import correct_enter
from correct_win import correct_win


def game_two_players():
    print("Первый игрок, ")
    first_player = player_name()
    print("Второй игрок, ")
    second_player = player_name()
    print(f"{first_player}, вы играете X, {second_player}, вы играете O. Начнем игру! \n");
    field = list(range(1, 10))
    fill_game_field(field)
    turn = 1
    while turn < 10:
        if turn % 2 != 0:
            print(f"{first_player}, твой ход!")
            player = first_player
            player_symbol = "X"
            correct_enter(player_symbol, field)
            fill_game_field(field)
        else:
            print(f"{second_player}, твой ход!")
            player = second_player
            player_symbol = "O"
            correct_enter(player_symbol, field)
            fill_game_field(field)
        if turn > 4:
            if correct_win(field):
                print(f"{player}, ты победил!")
                break
            elif turn == 9:
                print("Победила дружба!")
        turn += 1
