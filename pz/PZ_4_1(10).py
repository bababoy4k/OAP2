# 1. Дано целое число N (>0). Найти сумму N2 + (N + 1)² + (N+2)² + ... + (2N)²

n = int(input("Введите целое число N: "))

if n > 0:
    total_sum = 0
    for i in range(n+1, 2*n+1):
        total_sum += i**2
    print(f"Сумма = {total_sum}")
else:
    print("Пожалуйста, введите целое число больше нуля.")