# Gra w gorącego ziemniaka.
from Kolejka import Queue
import random

k=Queue()
k.engueue("Alan")
k.engueue("Damian")
k.engueue("Darek")
k.engueue("Włodek")
index=0
while k.size()>1:
    while index<random.randint(1,10):
        k.engueue(k.denqueue())
        index+=1
    k.denqueue()

print(k.denqueue())



