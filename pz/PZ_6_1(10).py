# Дан список А размера N и целое число К (1 <К <N). Вывести элементы список с порядковыми номерами, кратными К: Ак, А2*к, Аз*к,....

def print_elements_multiple_of_k(A, K):
    print("Элементы списка с порядковыми номерами, кратными", K, ": ", end="")
    print(*A[K-1::K], sep=", ")

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
K = int(input("Введите целое число К (1 < K < N): "))

if 1 < K < N:
    print_elements_multiple_of_k(A, K)
else:
    print("Пожалуйста, введите целое число K, которое удовлетворяет условию 1 < K < N.")