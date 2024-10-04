#1.	В последовательности на n целых чисел найти и вывести:
#1.	максимальный среди отрицательных
#2.	элементы кратные двум
#3.	их сумму

# Ввод последовательности чисел
n = int(input("Введите количество чисел в последовательности: "))
sequence = [int(x) for x in input("Введите последовательность чисел через пробел: ").split()]

# Поиск максимального среди отрицательных чисел
max_negative = None
for number in sequence:
    if number < 0:
        if max_negative is None or number > max_negative:
            max_negative = number

# Поиск элементов, кратных двум, и их сумма
multiples_of_two = []
sum_of_multiples = 0
for number in sequence:
    if number % 2 == 0:
        multiples_of_two.append(number)
        sum_of_multiples += number

# Вывод результатов
print("Максимальный среди отрицательных:", max_negative)
print("Элементы, кратные двум:", multiples_of_two)
print("Сумма элементов, кратных двум:", sum_of_multiples)
