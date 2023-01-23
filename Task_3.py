# 2. Старший и младший
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.

listFriends = {}
amount = int(input('Введите количество друзей: '))
for i in range(amount):
    name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    listFriends[name] = age

print (listFriends)

min_value = min(listFriends.values())
for name, am in listFriends.items():
    if am == min_value:
        print('Младше всех: ', name)