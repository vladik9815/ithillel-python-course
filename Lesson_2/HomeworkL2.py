#вводим наши данные
user_input = input("Какой расход у вашего авто в на 100 км?")
fuel_consumption = float(user_input)

user_input = input("Укажите дистанцию, сколько нужно проехать")
distance = float(user_input)

print(f"Расход топлива вашего авто {fuel_consumption}")
print(f"Ваша дистанция {distance}")

#Сколько литров, тратит на дистанцию
consumption_for_any_distance = (fuel_consumption / 100) * distance
print(f"Машина потратила {consumption_for_any_distance} литров на заявленную дистанцию")

fuel_cost_per_liter_UAH = 40

#Узнаем наш расход
our_rate = (fuel_consumption / 100) * consumption_for_any_distance * fuel_cost_per_liter_UAH
print(f"Стоимость вашей поездки составялет {our_rate} UAH")

#Хотел попробовать так, чтобы округлить сразу, но ругается на стринг :) отдельно не писал "print(round(our_rate, 2))"
# print(round(f"Стоимость вашей поездки составялет {our_rate, 2} UAH")



