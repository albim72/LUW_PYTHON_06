#działanie pthon GIL - oparte na ograniczeniach CPU
import time

wynik = []
s = time.perf_counter()
for x in range(100_000_000):
    wynik.append(x**2+10)
k = time.perf_counter()

print(f"czas CPU: {k-s} s")

print("_"*70)
import numpy as np

s = time.perf_counter()
dane = np.arange(0,100_000_000,1)

wynik = dane**2+10
k = time.perf_counter()
print(f"czas CPU: {k-s} s")
print("_"*70)

