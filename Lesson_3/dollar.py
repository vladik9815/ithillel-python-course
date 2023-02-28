usd_to_uah = 40

user_input = input("Сколько USD вы хотите продать?")

amount_usd = float(user_input)

# сообщаем пользователю исходные данные
print(f"У вас есть {amount_usd} USD, вы хотите их продавать")

# считаем результат
amount_uah = usd_to_uah * amount_usd

# выводим результат
print(f"Вы продали {amount_usd} USD и получили {amount_uah} UAH")
