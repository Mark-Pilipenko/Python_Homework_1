# 4 Напишите программу, 
# которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

b = True
while b == True:
    number = int(input('Введите номер четверти: '))
    if number > 4 or number < 1:
        print('Такой четверти не существует, попробуйте еще раз.')
    elif number == 1:
        print('x > 0')
        print('y > 0')
        b = False
    elif number == 2:
        print('x < 0')
        print('y > 0')
        b = False
    elif number == 3:
        print('x < 0')
        print('y < 0')
        b = False
    elif number == 4:
        print('x > 0')
        print('y < 0')
        b = False