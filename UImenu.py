from correct_choice import correct_enter_choice
from game_two_players import game_two_players
from game_with_bot import game_with_bot


def menu():
    print("Давайте начнем игру! Как вы ходите играть?\n\
            1 - игрок VS игрок;\n\
            2 - игрок VS бот")
    choice = correct_enter_choice()
    if choice == 1:
        game_two_players()
    else:
        game_with_bot()
