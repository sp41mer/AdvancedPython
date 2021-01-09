# Урок 7: декораторы

import functools
import time


# Декоратор - это функция, которая принимает функцию
# и возвращает новую функцию
def timer(func):
    # wraps сохраняет имя и документацию исходной функции
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        result = func(*args, **kwargs)
        elapsed = time.monotonic() - start
        print(f"{func.__name__} заняла {elapsed:.4f} сек")
        return result
    return wrapper


# Запись @timer означает: slow_sum = timer(slow_sum)
@timer
def slow_sum(n):
    return sum(range(n))


slow_sum(1_000_000)


# Декоратор с параметром - это функция, которая возвращает декоратор
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(times=3)
def greet(name):
    print(f"Привет, {name}!")


greet("класс")


# Готовый полезный декоратор из стандартной библиотеки: кэширование.
# Повторный вызов с теми же аргументами не считается заново
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# Без кэша fib(35) считался бы секунды, с кэшем - мгновенно
print(fib(35))
