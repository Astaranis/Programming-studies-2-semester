"""Zadanie 1. Zaproponuj rekurencyjny algorytm obliczania silni dla liczby całkowitej dodatniej n.
𝑛! = {
1 dla 𝑛 = 0
𝑛 ∗ (𝑛 − 1)! dla 𝑛 ≥ 1
"""

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)