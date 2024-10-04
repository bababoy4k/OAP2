# Дан список размера N. Найти количество его промежутков монотонности (то есть участков, на которых его элементы возрастают или убывают).

def count_monotonic_intervals(lst):
    monotonic_intervals = 0
    
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1] or lst[i] < lst[i-1]:
            monotonic_intervals += 1
    
    return monotonic_intervals

numbers = [1, 2, 3, 2, 5, 7, 4, 3, 1, 1]
intervals_count = count_monotonic_intervals(numbers)
print("Количество промежутков монотонности в списке:", intervals_count)

