from player_name import player_name
from game_field import fill_game_field
from correct_element import correct_enter
from turn_bot import turn_bot
from correct_win import correct_win


def game_with_bot():
    print("Игрок, ")
    player = player_name()
    print(f"{player}, вы играете X, Бот играет O. Начнем игру! \n");
    field = list(range(1, 10))
    fill_game_field(field)
    turn = 1
    while turn < 10:
        if turn % 2 != 0:
            print(f"{player}, твой ход!")
            player = player
            player_symbol = "X"
            correct_enter(player_symbol, field)
            fill_game_field(field)
        else:
            print("Очередь бота")
            player = "Бот"
            bot_sym = "O"
            turn_bot(field, player_symbol, bot_sym)
            fill_game_field(field)
        if turn > 4:
            if correct_win(field):
                print(f"{player}, ты победил")
                break
            elif turn == 9:
                print("Победила дружба!")
        turn += 1
