# Размер шахматной доски
size = 9

# Генерация шахматной доски
for row in range(size):
    for col in range(size):
        if (row + col) % 2 == 0:
            print(" ", end=" ")  # Белая клетка
        else:
            print("*", end=" ")  # Чёрная клетка
    print()  # Переход на новую строку после каждой строки доски
