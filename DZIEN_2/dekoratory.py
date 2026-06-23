#funkcja w typie dekoratora
from multiprocessing.dummy import DummyProcess


def startstop(funkcja):
    def wrapper(*args,**kwargs):
        print("start funkcji....")
        funkcja(*args,**kwargs)
        print("koniec funkcji....")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka...")

zawijanie("cukierków")

print("_"*70)

#prosty dekorator
zw = startstop(zawijanie)
zw("czekoladek")
print("_"*70)

startstop(zawijanie)("bułek")
print("_"*70)

#pełny dekorator
@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} ... na urodziny")

dmuchanie("świeczek")
print("_"*70)
dmuchanie("balonów")
print("_"*70)
