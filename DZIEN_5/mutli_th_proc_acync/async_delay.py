import time
import asyncio

def task(name,delay):
    print(f"starting {name} in {delay} seconds")
    time.sleep(delay)
    print(f"finished {name}")

async def atask(name,delay):
    print(f"starting {name} in {delay} seconds")
    await asyncio.sleep(delay)
    print(f"finished {name}")

def main():
    task("task1",2)
    task("task2",1)
    task("task3",3)


async def main_a():
    await asyncio.gather(
    atask("task1",2),
    atask("task2",1),
    atask("task3",3),
    )

if __name__ == '__main__':
    print("_"*70)
    print("synchronicznie")
    s = time.perf_counter()
    main()
    e = time.perf_counter()
    print(f"synchronicznie: {e-s}")

    print("_" * 70)
    print("asynchronicznie")
    st = time.perf_counter()
    asyncio.run(main_a())
    et = time.perf_counter()
    print(f"asynchronicznie: {et - st}")
