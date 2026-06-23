import time

#przykład 1
def pomiarczasu(funkcja):
    def wrapper(*args):
        starttime = time.time()
        print(funkcja(*args))
        endtime = time.time()
        wynik = endtime - starttime
        print(f"czas wykonania funkcji: {wynik} s")
    return wrapper

@pomiarczasu
def biglista():
    sum([i**5 for i in range(10_000_000)])

biglista()


# @pomiarczasu
# def seclista():
#     sum([i+522 for i in range(100_000_000)])
#
# seclista()

@pomiarczasu
def policz(a,b,c):
    return a+b+c*1990

policz(34,4454,6657)

