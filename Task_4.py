# 3. Еще немного о друзьях
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Выведите средний возраст всех друзей и самое длинное имя.

listFriends = {}
listAge = []
amount = int(input('Введите количество друзей: '))
for i in range(amount):
    name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    listFriends[name] = age
    listAge.append (age)

print (listAge)
print (listFriends)
print('Самое длинное имя: ', max(listFriends, key=len))

sum = 0
for i in listAge:
    sum = sum+i
x = sum/amount

print ('Средний возраст всех друзей:', x)


