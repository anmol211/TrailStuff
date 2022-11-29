import timeit
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed, TimeoutError
from multiprocessing import cpu_count

PRIMES = [n for n in range(100000)]


def is_prime(n):
    for i in range(2, n):
        continue
    return True


def stop_process_pool(executor):
    for pid, process in executor._processes.items():
        process.terminate()


def main():
    t1 = timeit.default_timer()
    print(cpu_count())
    res = []
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(is_prime, 100000001), executor.submit(is_prime, 10000001),
                   executor.submit(is_prime, 100000001),
                   executor.submit(is_prime, 10000001), executor.submit(is_prime, 10000001),
                   executor.submit(is_prime, 10000001),
                   executor.submit(is_prime, 10000001), executor.submit(is_prime, 10000001),
                   executor.submit(is_prime, 10000001), executor.submit(is_prime, 10000001),
                   executor.submit(is_prime, 10000001), executor.submit(is_prime, 10000001),
                   executor.submit(is_prime, 10000001),
                   executor.submit(is_prime, 10000001)]
        try:
            for future in as_completed(futures, timeout=1.5):
                res.append(future.result())

        except TimeoutError as e:
            print(e)
            print("{} in context".format(timeit.default_timer() - t1))
            stop_process_pool(executor)
        finally:
            executor.shutdown()
            print("{} in finally".format(timeit.default_timer() - t1))

    print(res)

    print("{} Seconds Needed for ProcessPoolExecutor".format(timeit.default_timer() - t1))

    # t2 = timeit.default_timer()
    # with ThreadPoolExecutor(max_workers=4) as executor:
    #     for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
    #         print('%d is prime: %s' % (number, prime))
    # print("{} Seconds Needed for ThreadPoolExecutor".format(timeit.default_timer() - t2))
    #
    t3 = timeit.default_timer()
    is_prime(10000001)
    is_prime(10000001)
    is_prime(10000001)
    is_prime(10000001)
    is_prime(10000001)
    is_prime(10000001)
    is_prime(10000001)
    is_prime(10000001)
    is_prime(10000001)
    is_prime(10000001)
    is_prime(10000001)
    is_prime(10000001)
    is_prime(10000001)
    is_prime(10000001)
    print("{} Seconds needed for single threaded execution".format(timeit.default_timer() - t3))


if __name__ == '__main__':
    t4 = timeit.default_timer()
    a = main()
    print(a)
    print("{} Seconds needed for main end".format(timeit.default_timer() - t4))
