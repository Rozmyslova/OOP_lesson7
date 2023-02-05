def correct_enter(symbol, field):
    correct_cell = False
    while not correct_cell:
        cell = input(f"Введите номер ячейки (1 to 9) для {symbol} = ")
        if not cell.isdigit():
            print("Вы ввели не номер")
            continue
        else:
            cell = int(cell)
            if 0 < cell < 10:
                if str(field[cell - 1]) in "XO":
                    print("Эта ячейка занята. Выберете другую ячейку ")
                    continue
                else:
                    field[cell - 1] = symbol
                    correct_cell = True
            else:
                print("Такой ячейки нет! ")
