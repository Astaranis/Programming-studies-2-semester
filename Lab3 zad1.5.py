"""Zadanie 5. Zapoznaj się z problemem wieży Hanoi, a następnie zaproponuję listę kroków, schemat
blokowy oraz implementację algorytmu."""

def hanoi(n, start, pomoc, cel):
    if n == 1:
        print("Przenieś krążek z igły", start, "na igłę", cel)
    else:
        hanoi(n-1, start, cel, pomoc)
        print("Przenieś krążek z igły", start, "na igłę", cel)
        hanoi(n-1, pomoc, start, cel)

# przykład użycia
hanoi(3, 'A', 'B', 'C')