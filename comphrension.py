import random
import timeit

# List comprehension
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i for i in original_prices if i > 0]
print(prices)
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)

# performance map <> list_comp <> loop
TAX_RATE = .08
txns = [random.randrange(100) for _ in range(1000)]
g_txns = (random.randrange(100) for _ in range(1000))  # generator expression


def get_price_with_generator():
    return list(map(get_price, g_txns))


def get_price(txn):
    return txn * (1 + TAX_RATE)


def get_prices_with_map():
    return list(map(get_price, txns))


def get_prices_with_comprehension():
    return [get_price(txn) for txn in txns]


def get_prices_with_loop():
    prices = []
    for txn in txns:
        prices.append(get_price(txn))
    return prices


def get_prices_with_filer():
    return list(filter(lambda x: x > 50, txns))


print(timeit.timeit(get_prices_with_comprehension, number=100))

print(timeit.timeit(get_price_with_generator, number=100))

print(timeit.timeit(get_prices_with_map, number=100))

print(timeit.timeit(get_prices_with_loop, number=100))

print(timeit.timeit(get_prices_with_filer, number=100))
