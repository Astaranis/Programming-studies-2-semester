"""Zadanie 4. Dana jest tablica n liczb całkowitych. Przedstaw algorytm liczący sumę elementów w
tablicy z zastosowaniem metody „dziel i zwyciężaj”."""

##############################################

def sum_dziel_i_zwyciezaj(arr, l, r):
    if l == r:
        return arr[l]

    mid = (l + r) // 2
    left_sum = sum_dziel_i_zwyciezaj(arr, l, mid)
    right_sum = sum_dziel_i_zwyciezaj(arr, mid + 1, r)

    return left_sum + right_sum

###################################################

# Przykład użycia:
arr = [1, 3, 5, 7, 9, 11, 13]
result = sum_dziel_i_zwyciezaj(arr, 0, len(arr) - 1)
print("Suma elementów tablicy:", result)

###########################################

#Michał Borowski