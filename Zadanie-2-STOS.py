#Zadanie 2. Zapoznaj się z poniższym algorytmem sprawdzania poprawności nawiasów i zaproponuj
#jego rozwiązanie (implementacja w Python oraz schemat blokowy).
from Stos1 import Stack

def parChecker (symbolString):
    s=Stack()
    balanced=True
    index=0
    while index<len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else :
            if s.isEmpty():
                balanced = False
            else :
                s.pop()
        index+=1

    if balanced and s.isEmpty():
        return True
    else :
        return False

print(parChecker('((()))'))
print(parChecker('(((())))'))
print(parChecker('((()())))'))
print(parChecker('(()()())(()))))'))
