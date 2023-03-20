def find_min_in_rows(arr):
    for i in range(len(arr)):
        min_value = arr[i][0]
        min_index = 0
        for j in range(len(arr[i])):
            if arr[i][j] < min_value:
                min_value = arr[i][j]
                min_index = j
        arr[i][0], arr[i][min_index] = arr[i][min_index], arr[i][0]
    return arr

# przykładowe użycie
arr = [[3, 2, 5], [1, 6, 4], [7, 8, 9]]
modified_arr = find_min_in_rows(arr)
print(modified_arr)