def lexicographic_sort(numbers):
    for i in range(1, len(numbers)):
        key = str(numbers[i])
        j = i - 1
        while j >= 0 and str(numbers[j]) > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = int(key)
    return numbers

numbers = [20, 3, 102, 45, 1001]
sorted_numbers = lexicographic_sort(numbers)
print(sorted_numbers)