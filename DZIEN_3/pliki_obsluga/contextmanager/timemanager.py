import time

class TimeManager:
    def __enter__(self):
        print('start pomiaru czasu...')
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.elapsed = self.end - self.start

        print(f"czas wykonania: {self.elapsed:.4f} sekundy ")
        return False

with TimeManager():
    total=0
    for i in range(10_000_000):
        total+=1
    print(f"suma: {total}")
