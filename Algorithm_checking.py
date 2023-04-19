"""3. Narysuj schemat blokowy algorytmu, który sprawdza czy podana przez użytkownika wartość
występuje w tablicy jednowymiarowej. Autor Michał Borowski"""


# Dodajemy narzędzia wymagane do przeprowadzenia zadania.
import numpy as np
Wartość_użytkownika = int(input(" Wpisz szukaną wartość "))

#####################################################################
# Tworzymy Tablice
Jakaś_tam_tablica = np.array([1,2,3,4,5,6,7,8,9,10])

######################################################################

# Tworzymy Algorytm sprawdzający
for algorytmy_zadanie_3 in Jakaś_tam_tablica:
    if algorytmy_zadanie_3 == Wartość_użytkownika:
        print("Ta wartość znajduje się w Tablicy")
        break
    else:
        print("Tej wartości nie ma w tablicy")
        break
