def correct_enter_choice():
    correct_choice = False
    while not correct_choice:
        choice = input("Ваш выбор: ")
        if not choice.isdigit():
            print("Вы ввели не число!")
            continue
        else:
            choice = int(choice)
            if (choice == 1) or (choice == 2):
                return choice
                correct_choice = True
            else:
                print("Такого пункта нет!")
                continue

