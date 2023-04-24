# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random
from datetime import timedelta
import math

while True:                                                 #Исключим повторение песен
    song1 = random.choice(my_favorite_songs)
    song2 = random.choice(my_favorite_songs)
    song3 = random.choice(my_favorite_songs)
    if song1 != song2 and song2 != song3 and song1 != song3:
        break
songs = song1 [0] +", " + song2 [0] + ", " + song3 [0]        #Определим список песен
t1 = math.modf(song1 [1])                                     #Определим время звучания
t2 = math.modf(song2 [1])
t3 = math.modf(song3 [1])
time = timedelta(minutes = t1[1], seconds = t1[0] * 100 ) + timedelta(minutes = t2[1], seconds = t2[0] * 100 ) + timedelta(minutes = t3[1], seconds = t3[0] * 100 )
print("Выбраны песни", songs, "и они звучат", time)

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

while True:                                                 #Исключим повторение песен
    song1 = key1, val1 = random.choice(list(my_favorite_songs_dict.items()))
    song2 = key2, val2 = random.choice(list(my_favorite_songs_dict.items()))
    song3 = key3, val3 = random.choice(list(my_favorite_songs_dict.items()))
    if song1 != song2 and song2 != song3 and song1 != song3:
        break
songs = key1 +", " + key2 + ", " + key3        #Определим список песен
t1 = math.modf(val1)                           #Определим время звучания
t2 = math.modf(val2)
t3 = math.modf(val3)
t = timedelta(minutes = t1[1], seconds = t1[0] * 100 ) + timedelta(minutes = t2[1], seconds = t2[0] * 100 ) + timedelta(minutes = t3[1], seconds = t3[0] * 100 )
print("Из словаря выбраны песни", songs, "и они звучат", t)

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

# Да! Интересное решение! У меня был вот такой вариант
# ###################### Решение ######################

# Импорты
from random import sample
from datetime import timedelta
from math import modf

# Пункт А
time = my_favorite_songs[0][1] + my_favorite_songs[2][1] + my_favorite_songs[4][1]
print(f'Пункт А: Три песни звучат {time} минут.')

# Пункт С(А)
time = 0
for song in sample(my_favorite_songs, 3):
    time += song[1]

print(f'Пункт C(A): Три песни звучат {round(time, 2)}')

# Пункт D(А)
total_time = timedelta()
for song in sample(my_favorite_songs, 3):
    s, m = modf(song[1])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Пункт D(A): Три песни звучат {total_time}')


# Пункт B
time = my_favorite_songs_dict['Waste a Moment'] + my_favorite_songs_dict['Staying\' Alive'] + my_favorite_songs_dict['Easy']
print(f'Пункт B: Три песни звучат {time} минут.')

# Пункт C(B)
time = 0
for song in sample(tuple(my_favorite_songs_dict), 3):
    time += my_favorite_songs_dict[song]

print(f'Пункт C(B): Три песни звучат {round(time, 2)}')

# Пункт D(B)
total_time = timedelta()
for song in sample(tuple(my_favorite_songs_dict), 3):
    s, m = modf(my_favorite_songs_dict[song])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))
