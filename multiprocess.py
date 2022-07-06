import timeit
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from multiprocessing import cpu_count
PRIMES = [n for n in range(100000)]


def is_prime(n):
    for i in range(2, n):
        continue


def main():
    t1 = timeit.default_timer()
    print(cpu_count())
    with ProcessPoolExecutor(max_workers=1) as executor:
        futures = [executor.submit(is_prime, 10000001), executor.submit(is_prime, 10000001), executor.submit(is_prime, 10000001),
                   executor.submit(is_prime, 10000001),executor.submit(is_prime, 10000001), executor.submit(is_prime, 10000001),
                   executor.submit(is_prime, 10000001),executor.submit(is_prime, 10000001), executor.submit(is_prime, 10000001), executor.submit(is_prime, 10000001),
                   executor.submit(is_prime, 10000001),executor.submit(is_prime, 10000001), executor.submit(is_prime, 10000001),
                   executor.submit(is_prime, 10000001)]
        for future in as_completed(futures):
            print(future.result())

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
    main()
