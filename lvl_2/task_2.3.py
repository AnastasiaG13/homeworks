# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    numbers = {1: "One",
               2: "Two",
               3: "Three",
               4: "Four",
               5: "Five",
               6: "Six",
               7: "Seven",
               8: "Eigth",
               9: "Nine"}
    return numbers.get(number)

n=10
print(switch_it_up(n))