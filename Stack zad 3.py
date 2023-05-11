#Zadanie 3. Zaproponuj algorytm sprawdzania poprawności różnych symbol

from Stos1 import Stack

def sprawdz_poprawnosc(symbolString):
    stos = Stack()
    for symbol in symbolString:
        if symbol in "([{":
            stos.push(symbol)
        elif symbol in ")]}":
            if stos.isEmpty():
                return False
            poprzedni_symbol = stos.pop()
            if not czy_pasuje(poprzedni_symbol, symbol):
                return False
    return stos.isEmpty()

def czy_pasuje(otwarty, zamkniety):
    if otwarty == "(" and zamkniety == ")":
        return True
    elif otwarty == "[" and zamkniety == "]":
        return True
    elif otwarty == "{" and zamkniety == "}":
        return True
    else:
        return False

# Przykładowe użycie
print(sprawdz_poprawnosc("(({}[])[])"))  # Wynik: True
print(sprawdz_poprawnosc("([)]"))  # Wynik: False