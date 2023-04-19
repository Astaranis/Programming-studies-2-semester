"""5. Zaprojektuj algorytm wyszukiwania w tablicy dwuwymiarowej minimalnej wartości w każdym
wierszu. Po znalezieniu minimalnej wartości wstaw ją na początek danego wiersza (poprzez
zamianę miejsc)."""

import numpy as np
T2W = np.array([[1,2,3,5,-2],[6,7,8,9,-10]])
T2W2 = T2W

a = (T2W[0][0])
b = (T2W[1][0])
i=-1
for m in T2W[0]:
    i+=1
    if m < a:
        T2W2[0][0] = T2W2[0][i]

        T2W2[0][i] = a

        T2W2[1][0] = T2W2[1][i]

        T2W2[1][i] = b


print(T2W2)
