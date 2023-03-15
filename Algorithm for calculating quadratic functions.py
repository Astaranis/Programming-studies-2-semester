import math
"Implementacja algorytmu w języku Python, Autor Michał Borowski"
a=int(input("Podaj wartość a: "))
b=int(input("Podaj wartość b: "))
c=int(input("Podaj wartość c: "))
print(" Rozwiązuje równanie kwadratowe :",a,"x**2",b,"x",c,end="\n")
if a!=0:
    delta = b**2 - 4*a*c
    print("delta wynosi :",(int(delta)))
    if delta == 0 :
        x1 = -b/(2*a)
        print("Funkcja posiada tylko jeden pierwiastek i jego wartość to :",(x1))
        exit()
    elif delta > 0:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        print("Pierwiastki funkcji to  ","x1 :", (x1),"oraz x2 : ",(x2) )
        exit()
    else:
        print("Brak Pierwiastków funkcji kwadratowej")
        exit()







else:
    print("to nie jest równanie kwadratowe")
    exit()