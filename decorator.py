import functools


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__}")
        return func(*args, **kwargs)

    print("hii")
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


@count_calls
def say_whee():
    print("Whee!")


say_whee()
say_whee()


#############
def sort_list(func):
    def wrapper(arr):
        a = func(arr)
        return sorted(a)

    return wrapper


@sort_list
def hello(arr: list):
    return arr


print(hello([2, 4, 1, 3, 5, 7]))