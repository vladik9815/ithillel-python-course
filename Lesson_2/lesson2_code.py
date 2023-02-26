import math  # import libary. чтобы округлять всегда в какую-то сторону

# math.ceil()  #округлять всегда вверх

# создаем переменную
a = int()  # целое число
b = float()  # десятичные числа

print(a, b)

a = 2
b = 2.5
print(a, b)
print(type(a),  type(b))  # узнать тип

a = 2 + 5
print(a)
a = 3 - 1
print(a)
a = 38 * 2
print(a)
a = 38 / 2
print(a, type(a))  # деление всегда флоат. узнаем так тип.

a = int(38 / 2) # делаем переменную интом
print(a, type(a))

print(int(1.75)) # инт обрезает десятичную часть
print(round(1.75)) # округляет число round

a = 10 / 3
print(round(a, 2)) # показать 2 числа после запятой

b = 20 / 3
print(round(b, 2))

#  name = input("Enter your name: ")
#  print(f'Hi {name}!')

a = 25 / 6
print(round(a, 2))
print(math.ceil(8.3))  # округлит число до 9

print(float(int(1.75)))  # округлит до 1, но уже 1.0 будет
print(int(1.75))

b = 5 ** 2  # возвести в степень
print(b)

b = pow(3, 4)  # тоже возвести в степень
print(b)

c = pow(10, 2)
print(c)

c = pow(25, 1 / 2)  # корень
print(int(c)) # если не ставить инт, выведит как флоат

print(math.sqrt(36))  # квадратный корень
y = 5 ** 2
print(y)
y = pow(5, 2)
print(y)
print(math.sqrt(36))
y = pow(36, 1 / 2)
print(y)

x = 25 * 3 - 2 / 4 - 2 # в питоне считает по приоритетам(как в математике)
print(x)

unlucky_ticket = 938984
lucky_ticket = 123501  # в сумме 3 числа, должны быть одинаковыми

left_side = unlucky_ticket // 1000  # поделит на 1000. 3 цифры последних уберет
print(left_side)
right_side = unlucky_ticket % 1000  # остаток от деления
print(right_side)





















