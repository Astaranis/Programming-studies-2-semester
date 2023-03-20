import numpy as np
Wartość = int(input(" Wpisz szukaną wartość "))

# Tworzymy Tablice
Tablica = np.array([1,2,3,4,5,6,7,8,9,10])


for algorytmy_zadanie_3 in Tablica:
    if algorytmy_zadanie_3 == Wartość:
        print("Ta wartość znajduje się w Tablicy")
else:
    print("Tej wartości nie ma w tablicy")
