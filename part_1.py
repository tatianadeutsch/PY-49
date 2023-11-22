import logging

logging.basicConfig(level=logging.INFO, filename="part_1.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

# 3.
"""
Напишите программу для подсчета среднего числа всех 
введенных пользователям чисел. 
Ввод пользователя должен осуществляться с помощью input. 
Если пользователь вводит ноль, то выводиться на экран среднее значение. 
Используйте цикл while для решения данной задачи
"""

try:
    number_user = int(input("Введите число: \n"))
    sum_numbers = 0
    count = 0

    while number_user != 0:
            count += 1
            sum_numbers += number_user
            number_user = int(input("Введите число: \n"))
    print(f"Среднее значение из {count} введенных чисел (!=0): {round(sum_numbers / count, 2)}")

    logging.info(f"Среднее значение из {count} введенных чисел (!=0): {round(sum_numbers / count, 2)}")

except (ZeroDivisionError, ValueError):
    logging.error("Неверное значение или деление на ноль", exc_info=True)
    print("Неверное значение или деление на ноль.")


# 4.
"""
Напишите программу для вывода на экран чисел от 0 до 100
Вам понадобиться цикл for, конструкция range и print
"""

for number in range(0,101):
    print(number)


# 5.
"""
Напишите программу для вывода таблицы умножения от 0 до 9. Используйте вложенный цикл for, print и range
Пример:
0*1 = 0
0 *2 = 0
…..
9*1 = 9
9*2=18
"""

for multiplier_1 in range(0,10):
    print("------")
    for multiplier_2 in range(1,10):
        multiplication = multiplier_1 * multiplier_2
        print(f"{multiplier_1} * {multiplier_2} = {multiplication}")


# 6.
"""
Создайте список с разными значениями, пройдитесь по нему в цикле 
и выведите на экран. 
(Сделайте тоже самое со словарем и выведите ключ и значение)
"""

from random import randint

list_numbers = [randint(20,50) for number in range(5)]
list_numbers_out = []
for i in list_numbers:
    list_numbers_out.append(i * 2)
print(f"Первоначальный список: {list_numbers}")
print(f"Список после итерации: {list_numbers_out}")


# dict
numbers = range(10)
dict_numbers = {n: n*2 for n in numbers if n != 0}
print(dict_numbers)



