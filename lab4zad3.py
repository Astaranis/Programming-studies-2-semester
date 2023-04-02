"""Zadanie 3. Stosując metodę "dziel i zwyciężaj", ułóż algorytm wyznaczania największego elementu
wektora."""


####################################################################

def find_max_dziel_i_zwyciezaj(arr, l, r):
    if l == r:
        return arr[l]

    mid = (l + r) // 2
    left_max = find_max_dziel_i_zwyciezaj(arr, l, mid)
    right_max = find_max_dziel_i_zwyciezaj(arr, mid + 1, r)

    return max(left_max, right_max)

######################################################################

# Przykład użycia:
arr = [1, 3, 5, 7, 9, 11, 13]
result = find_max_dziel_i_zwyciezaj(arr, 0, len(arr) - 1)
print("Największy element wektora:", result)


#########################################################
#Michał Borowski