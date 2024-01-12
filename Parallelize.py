from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import time

def func(iter):
    for i in range(iter):
        pass
    print("Done.")
    return iter


args = [100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000]

if __name__ == "__main__":
    multiprocessing.freeze_support() 

    t0 = time.time()

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(func, args))
        print(results)

    t1 = time.time()

    print(t1 - t0)

