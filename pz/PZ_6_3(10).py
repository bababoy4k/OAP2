# Дан список размера N. Осуществить сдвиг элементов список вправо на одну позицию (при этом А1 перейдет в А2, А2 — в Аз, ..., А-1 — в Ам, 
#а исходное значение последнего элемента будет потеряно). Первый элемент полученного списка положить равным 0.

def shift_right_with_zero(lst):
    shifted_list = lst[:-1]
    shifted_list.insert(0, 0)
    return shifted_list

numbers = [1, 2, 3, 4, 5]  
shifted_numbers = shift_right_with_zero(numbers)
print("Исходный список после сдвига вправо с добавлением 0:", shifted_numbers)

