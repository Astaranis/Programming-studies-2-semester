#algorytm wczytywania ciągu n liczb całkowitych (N>0) i wyznaczania ilości liczb
#ujemnych w tym ciągu. Autor Michał Borowski


ciag = []
ujemne = 0
liczba=int(input("Podaj liczbę cyfr w ciągu"))
for x in range(liczba):
    dodawanie = int(input("Podaj liczbę całkowitą jaką chcesz dodać do ciągu: "))
    ciag.append(dodawanie)
for r in ciag:
    if  r < 0 :
        ujemne +=1
print("W podanym ciągu znajduje się ",(ujemne),"cyfr ujemnych")


