#Zadanie 4. Napisz program czytający wyrażenie arytmetyczne w notacji postfiksowej (Odwrotna
#Notacja Polska) i obliczający jego wartość z wykorzystaniem stosu
from Stos1 import Stack

def Notacja(wyrazenie_arytmetyczne):
    s=Stack()


    ilosc=0

    while ilosc<len(wyrazenie_arytmetyczne):
        znak = wyrazenie_arytmetyczne[ilosc]

        if znak in ["+","-","*","^","/","="]:

            if znak == "+":
                j=s.pop()
                k=s.pop()
                s.push(j+k)

            elif znak == "-":
                j=s.pop()
                k=s.pop()
                s.push(k-j)
            elif znak == "*":
                j=s.pop()
                k=s.pop()
                s.push(j*k)
            elif znak == "^":
                j=s.pop()
                k=s.pop()
                s.push(k**j)
            elif znak == "/":
                j=s.pop()
                k=s.pop()
                s.push(k/j)
            elif znak == "=":
                return s.pop()

        else:
            s.push(znak)


        ilosc += 1

print(Notacja([7,3,"+",5,2,"-",2,"^","*","="]))

