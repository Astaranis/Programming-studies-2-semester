def suma_fragmentu(A, lewy_indeks, prawy_indeks):
    if lewy_indeks == prawy_indeks:
        return A[lewy_indeks]
    else:
        srodkowy_indeks = (lewy_indeks + prawy_indeks) // 2
        lewa_suma = suma_fragmentu(A, lewy_indeks, srodkowy_indeks)
        prawa_suma = suma_fragmentu(A, srodkowy_indeks + 1, prawy_indeks)
        return lewa_suma + prawa_suma

A = [1, 2, 3, 4, 5]
wynik = suma_fragmentu(A, 0, len(A) - 1)
print(wynik)
