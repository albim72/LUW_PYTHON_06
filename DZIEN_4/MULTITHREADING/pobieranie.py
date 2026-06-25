import threading
import time

def download_file(name):
    print(f"pobieram {name}")
    time.sleep(2)
    print(f"zakończono pobieranie {name}")


threads = []

for filename in ["a.csv", "b.csv", "c.csv", "d.csv"]:
    thread = threading.Thread(target=download_file, args=(filename,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

print("wszystko pobrane")


def heavy_calculation():
    total = 0
    for i in range(40_000_000):
        total += i
    return total

start = time.time()

thread1 = threading.Thread(target=heavy_calculation)
thread2 = threading.Thread(target=heavy_calculation)
thread3 = threading.Thread(target=heavy_calculation)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
end = time.time()

print(f"czas...wykoania: {end-start:2f} s")
