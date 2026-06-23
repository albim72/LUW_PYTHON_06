# import opis as op
from opis import informacja,policz
from kalk import Kalkulator

print(informacja("algorytm ewolucyjny dla python"))
print(policz(4,6,32))

print("_"*70)
k = Kalkulator(11,8,56,3,18)
print(k.wartA())
print("_"*70)
print(k.wartB())
