
"""Zadanie 2. Napisz funkcję rekurencyjną, która odwraca elementy tablicy.
Np. Dane wejściowe: tablica: 1, 2, 3, 4, 5
Wyjście: tablica: 5, 4, 3, 2, 1
w pythonie"""

def odwroc_tablice(tablica):
    if len(tablica) == 0:
        return []
    else:
        return [tablica[-1]] + odwroc_tablice(tablica[:-1])