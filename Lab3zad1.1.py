"""Zadanie 1. Zapoznaj się z poniższym algorytmem NWD, a następnie zaproponuj schemat blokowy
algorytmu oraz jego implementację (rozwiązanie należy zaproponować w formie iteracyjnej
i rekurencyjnej)."""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(12, 18))
print(gcd(28, 24))