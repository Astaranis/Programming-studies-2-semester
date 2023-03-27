"""Zadanie 4. Zaproponuj rekurencyjny algorytm zamiany liczby dziesiętnej na binarną. Należy
zaprojektować schemat blokowy oraz implementacje."""

def dec_to_bin(n):
    if n == 0:
        return ""
    else:
        return dec_to_bin(n // 2) + str(n % 2)


    #################################################################