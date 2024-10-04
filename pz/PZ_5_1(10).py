# Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму его цифр и т. д. Через сколько таких действий получится нуль?

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def steps_to_zero(n):
    steps = 0
    
    while n != 0:
        n -= sum_of_digits(n)
        steps += 1
    
    return steps

number = int(input("Введите заданное число: "))
result = steps_to_zero(number)
print(f"Через {result} действий получится нуль.")
